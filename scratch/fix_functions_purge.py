import requests
import re
from html import unescape

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
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_f.text, re.DOTALL)
current = unescape(content_match.group(1))

purge_code = """

// 7. Instant LiteSpeed & Elementor Purge Trigger
add_action('init', function() {
    if (isset($_GET['purge_lscache_now'])) {
        if (defined('LSCWP_V')) {
            do_action('litespeed_purge_all');
        }
        if (class_exists('\\\\Elementor\\\\Plugin')) {
            \\\\Elementor\\\\Plugin::$instance->files_manager->clear_cache();
        }
        foreach (array(32, 33, 34, 35, 36, 37) as $pid) {
            delete_post_meta($pid, '_elementor_css');
        }
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
        }
        echo "PURGED_ALL_SUCCESS";
        exit;
    }
});
"""

new_content = current + purge_code
post_data = {
    'nonce': nonce,
    '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor',
    'action': 'update',
    'file': 'functions.php',
    'theme': 'hello-elementor',
    'newcontent': new_content,
    'submit': 'Update File'
}
r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data)
print("r_post status:", r_post.status_code)
print("r_post url:", r_post.url)
print("Success in text:", "File edited successfully" in r_post.text)

