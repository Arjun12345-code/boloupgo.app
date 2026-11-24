import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import re
from html import unescape
import time

session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

login_url = "https://boloupgo.app/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk"
r_login = session.post(login_url, data={
    'log': 'webdev',
    'pwd': 'a)Y%8quFdY^aTxtvrUESQs81',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.app/wp-admin/',
    'testcookie': '1'
}, timeout=30)
print("Login status:", r_login.status_code)

r_f = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor", timeout=30)
nonce_match = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_f.text)
if not nonce_match:
    print("Could not find nonce!")
    exit(1)
nonce = nonce_match.group(1)

content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_f.text, re.DOTALL)
if not content_match:
    print("Could not find textarea content!")
    exit(1)
current = unescape(content_match.group(1))

if "boloup_fix_all" in current:
    print("Already added boloup_fix_all to functions.php.")
else:
    fix_code = r'''

// 5. Automatic Hero Image Fix & Output Transform
add_action('template_redirect', function() {
    ob_start(function($html) {
        if (strpos($html, 'boloupgo-hero.png') !== false) {
            $html = str_replace(
                'https://boloupgo.app/wp-content/uploads/2026/11/boloupgo-hero.png',
                'https://boloupgo.app/wp-content/uploads/2026/11/boloupgo-app-nobg.png',
                $html
            );
            $html = str_replace('width="1243" height="1266"', 'width="1038" height="972"', $html);
        }
        return $html;
    });
}, 0);

// 6. DB Replacer & Cache Purge Endpoint
add_action('init', function() {
    if (isset($_GET['boloup_fix_all'])) {
        global $wpdb;
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE meta_value LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE post_content LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE meta_value LIKE '%width=\"1243\" height=\"1266\"%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE post_content LIKE '%width=\"1243\" height=\"1266\"%'");
        
        if (class_exists('Elementor\Plugin')) {
            \Elementor\Plugin::$instance->files_manager->clear_cache();
        }
        foreach (array(32, 33, 34, 35, 36, 37) as $pid) {
            delete_post_meta($pid, '_elementor_css');
        }
        if (defined('LSCWP_V')) {
            do_action('litespeed_purge_all');
        }
        if (function_exists('wp_cache_flush')) {
            wp_cache_flush();
        }
        echo "BOLOUP_FIX_ALL_SUCCESS";
        exit;
    }
});
'''
    new_content = current + fix_code
    post_data = {
        'nonce': nonce,
        '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor',
        'action': 'update',
        'file': 'functions.php',
        'theme': 'hello-elementor',
        'newcontent': new_content,
        'submit': 'Update File'
    }
    r_post = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data, timeout=30)
    print("Post status:", r_post.status_code)
    print("Success in URL or text:", "file-edited-successfully" in r_post.url or "File edited successfully" in r_post.text)
    if "error" in r_post.text.lower():
        notices = re.findall(r'<div[^>]*class="[^"]*notice[^"]*"[^>]*>(.*?)</div>', r_post.text, re.DOTALL)
        for n in notices:
            print("Notice:", re.sub(r'<[^>]+>', '', n).strip())

time.sleep(1)
r_trigger = session.get("https://boloupgo.app/?boloup_fix_all=1", timeout=30)
print("Trigger endpoint response:", r_trigger.status_code, r_trigger.text[:100])

time.sleep(1)
r_live = requests.get("https://boloupgo.app/?refresh=" + str(time.time()), timeout=30)
print("Live Home Status:", r_live.status_code)
print("Has boloupgo-app-nobg.png on live?", "boloupgo-app-nobg.png" in r_live.text)
print("Has boloupgo-hero.png on live?", "boloupgo-hero.png" in r_live.text)
