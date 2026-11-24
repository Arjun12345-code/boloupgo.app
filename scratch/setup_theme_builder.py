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

content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_f.text, re.DOTALL)
from html import unescape
current_content = unescape(content_match.group(1))

tb_snippet = """

// 6. Ensure Elementor Pro Theme Builder Conditions and Global Header/Footer
add_action('init', function() {
    if (isset($_GET['setup_tb'])) {
        // Option name in Elementor Pro is 'elementor_pro_theme_builder_conditions'
        $conditions = array(
            'header' => array(
                32 => array('include/general')
            ),
            'footer' => array(
                33 => array('include/general')
            )
        );
        update_option('elementor_pro_theme_builder_conditions', $conditions);
        update_post_meta(32, '_elementor_conditions', array('include/general'));
        update_post_meta(33, '_elementor_conditions', array('include/general'));
        
        if (class_exists('\\\\Elementor\\\\Plugin')) {
            \\\\Elementor\\\\Plugin::$instance->files_manager->clear_cache();
        }
        echo json_encode(array('success' => true, 'conditions' => get_option('elementor_pro_theme_builder_conditions')));
        exit;
    }
});
"""

if "setup_tb" not in current_content:
    new_content = current_content + tb_snippet
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
    print("Updated functions.php with setup_tb:", "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url)

r_trig = session.get("https://boloupgo.app/?setup_tb=1")
print("setup_tb result:", r_trig.status_code, r_trig.text[:300])

