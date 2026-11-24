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

# Append cache clear and force compile action
cache_clear_snippet = """

// 5. Elementor Cache Invalidator
add_action('init', function() {
    if (isset($_GET['clear_el_cache']) || !get_transient('boloup_el_cache_cleared_v2')) {
        if (class_exists('\\\\Elementor\\\\Plugin')) {
            \\\\Elementor\\\\Plugin::$instance->files_manager->clear_cache();
        }
        foreach (array(32, 33, 34, 35, 36, 37) as $pid) {
            delete_post_meta($pid, '_elementor_css');
        }
        set_transient('boloup_el_cache_cleared_v2', 1, DAY_IN_SECONDS);
    }
});
"""

if "boloup_el_cache_cleared_v2" not in current_content:
    new_content = current_content + cache_clear_snippet
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
    print("Updated functions.php with cache clear:", "File edited successfully" in r_post.text or "file-edited-successfully" in r_post.url)

# Trigger clear_el_cache
r_trig = session.get("https://boloupgo.app/?clear_el_cache=1")
print("Trigger status:", r_trig.status_code)

# Check rendered HTML
r_check = session.get("https://boloupgo.app/?clear_el_cache=1")
print("Has 'brand-logo'?", "brand-logo" in r_check.text)
print("Has 'footer-grid'?", "footer-grid" in r_check.text)
print("Has 'Live More. Connect More'?", "Live More. Connect More" in r_check.text)
print("Has 'Frequently Asked Questions'?", "Frequently Asked Questions" in r_check.text)
print("Has 'table-comparison'?", "table-comparison" in r_check.text)
print("HTML Size:", len(r_check.text))

