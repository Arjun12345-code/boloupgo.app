import requests
import re

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
session = requests.Session()
session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
})

r_f = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor")
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_f.text).group(1)

with open("scratch/hello_functions_original.php", "r", encoding="utf-8") as orig:
    original_code = orig.read()

# Custom snippet to append
custom_snippet = """

/* ==========================================================================
   BoloUp Go Custom Engine - SEO, Stylesheet Sync, & Output Control
   ========================================================================== */

// 1. Sync style.css to WordPress root directory
add_action('init', function() {
    $theme_style = get_template_directory() . '/style.css';
    $root_style  = ABSPATH . 'style.css';
    if (file_exists($theme_style)) {
        if (!file_exists($root_style) || filesize($root_style) !== filesize($theme_style)) {
            @copy($theme_style, $root_style);
        }
    }
});

// 2. Enqueue Custom CSS on front-end and Elementor canvas
add_action('wp_enqueue_scripts', function() {
    wp_enqueue_style(
        'boloup-go-main-style',
        get_template_directory_uri() . '/style.css',
        array(),
        '1.0.3'
    );
}, 99);

add_action('elementor/frontend/after_enqueue_styles', function() {
    wp_enqueue_style(
        'boloup-go-elementor-style',
        get_template_directory_uri() . '/style.css',
        array(),
        '1.0.3'
    );
});

// 3. Disable admin bar on front-end
add_filter('show_admin_bar', '__return_false');

// 4. Set Exact Meta Titles & Descriptions for SEO
function boloup_get_seo_data() {
    $uri = trim($_SERVER['REQUEST_URI'] ?? '', '/');
    // Remove query params
    $uri = explode('?', $uri)[0];

    $seo = array(
        '' => array(
            'title' => 'BoloUp Go – Live, Connect, Discover, and Earn More',
            'desc'  => 'Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.'
        ),
        'home' => array(
            'title' => 'BoloUp Go – Live, Connect, Discover, and Earn More',
            'desc'  => 'Discover BoloUp Go, a social entertainment app for live video, voice rooms, chat, gifts, and earning opportunities to join as a Host or Agent.'
        ),
        'host' => array(
            'title' => 'BoloUp Go Host – Go Live, Connect & Grow',
            'desc'  => 'Become a BoloUp Go Host, create live content, connect with viewers, receive gifts, and grow with agency support'
        ),
        'agent' => array(
            'title' => 'BoloUp Go Agent – Build & Grow Your Host Team',
            'desc'  => 'Become a BoloUp Go Agent, recruit Hosts, manage your network, support creators, and explore earning opportunities through team activity.'
        ),
        'contact' => array(
            'title' => 'Contact BoloUp Go – Support & Help',
            'desc'  => 'Contact BoloUp Go for help with your account, Host or Agent registration, withdrawals, agency questions, and other platform support.'
        )
    );

    return $seo[$uri] ?? null;
}

add_filter('pre_get_document_title', function($title) {
    $seo = boloup_get_seo_data();
    if ($seo && !empty($seo['title'])) {
        return $seo['title'];
    }
    return $title;
}, 999);

add_filter('wpseo_title', function($title) {
    $seo = boloup_get_seo_data();
    if ($seo && !empty($seo['title'])) {
        return $seo['title'];
    }
    return $title;
}, 999);

add_filter('wpseo_metadesc', function($desc) {
    $seo = boloup_get_seo_data();
    if ($seo && !empty($seo['desc'])) {
        return $seo['desc'];
    }
    return $desc;
}, 999);

// Add fallback meta description in wp_head if Yoast isn't outputting it
add_action('wp_head', function() {
    $seo = boloup_get_seo_data();
    if ($seo && !empty($seo['desc'])) {
        echo '<meta name="description" content="' . esc_attr($seo['desc']) . '">' . "\\n";
    }
}, 1);
"""

new_functions = original_code + custom_snippet

post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor',
    'newcontent': new_functions,
    'submit': 'Update File'
}

r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
success = "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url
print("Updated hello-elementor/functions.php:", success)

# Trigger init
session.get("https://boloupgo.app/wp-admin/")

# Test https://boloupgo.app/style.css
r_root = requests.get("https://boloupgo.app/style.css")
print("https://boloupgo.app/style.css status:", r_root.status_code, "Length:", len(r_root.text))

