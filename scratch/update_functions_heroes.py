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
}, timeout=30)

r_f = session.get("https://boloupgo.app/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor", timeout=30)
nonce = re.search(r'id="nonce"\s+name="nonce"\s+value="([^"]+)"', r_f.text).group(1)
content_match = re.search(r'<textarea[^>]*id="newcontent"[^>]*>(.*?)</textarea>', r_f.text, re.DOTALL)
current = unescape(content_match.group(1))

# Update the template_redirect buffer function to handle all 3 heroes
old_ob_block = r'''// 5. Automatic Hero Image Fix & Output Transform
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
}, 0);'''

new_ob_block = r'''// 5. Automatic Hero Image Fix & Output Transform
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
        if (strpos($html, 'boloup-host-cutout.png') !== false) {
            $html = str_replace(
                'https://boloupgo.app/wp-content/uploads/2026/11/boloup-host-cutout.png',
                'https://boloupgo.app/wp-content/uploads/2026/11/boloup-host-nobg.png',
                $html
            );
            $html = str_replace('width="1553" height="1457"', 'width="798" height="811"', $html);
        }
        if (strpos($html, 'boloup-agent-full.png') !== false) {
            $html = str_replace(
                'https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-full.png',
                'https://boloupgo.app/wp-content/uploads/2026/11/boloup-agent-nobg.png',
                $html
            );
            $html = str_replace('width="1458" height="1210"', 'width="610" height="715"', $html);
        }
        return $html;
    });
}, 0);'''

old_db_block = r'''        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE meta_value LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE post_content LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE meta_value LIKE '%width=\"1243\" height=\"1266\"%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE post_content LIKE '%width=\"1243\" height=\"1266\"%'");'''

new_db_block = r'''        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE meta_value LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloupgo-hero.png', 'boloupgo-app-nobg.png') WHERE post_content LIKE '%boloupgo-hero.png%'");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE meta_value LIKE '%width=\"1243\" height=\"1266\"%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'width=\"1243\" height=\"1266\"', 'width=\"1038\" height=\"972\"') WHERE post_content LIKE '%width=\"1243\" height=\"1266\"%'");
        
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloup-host-cutout.png', 'boloup-host-nobg.png') WHERE meta_value LIKE '%boloup-host-cutout.png%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloup-host-cutout.png', 'boloup-host-nobg.png') WHERE post_content LIKE '%boloup-host-cutout.png%'");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'width=\"1553\" height=\"1457\"', 'width=\"798\" height=\"811\"') WHERE meta_value LIKE '%width=\"1553\" height=\"1457\"%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'width=\"1553\" height=\"1457\"', 'width=\"798\" height=\"811\"') WHERE post_content LIKE '%width=\"1553\" height=\"1457\"%'");

        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'boloup-agent-full.png', 'boloup-agent-nobg.png') WHERE meta_value LIKE '%boloup-agent-full.png%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'boloup-agent-full.png', 'boloup-agent-nobg.png') WHERE post_content LIKE '%boloup-agent-full.png%'");
        $wpdb->query("UPDATE {$wpdb->postmeta} SET meta_value = REPLACE(meta_value, 'width=\"1458\" height=\"1210\"', 'width=\"610\" height=\"715\"') WHERE meta_value LIKE '%width=\"1458\" height=\"1210\"%'");
        $wpdb->query("UPDATE {$wpdb->posts} SET post_content = REPLACE(post_content, 'width=\"1458\" height=\"1210\"', 'width=\"610\" height=\"715\"') WHERE post_content LIKE '%width=\"1458\" height=\"1210\"%'");'''

if old_ob_block in current:
    current = current.replace(old_ob_block, new_ob_block)
    current = current.replace(old_db_block, new_db_block)
    
    post_data = {
        'nonce': nonce,
        '_wp_http_referer': '/wp-admin/theme-editor.php?file=functions.php&theme=hello-elementor',
        'action': 'update',
        'file': 'functions.php',
        'theme': 'hello-elementor',
        'newcontent': current,
        'submit': 'Update File'
    }
    r_up = session.post("https://boloupgo.app/wp-admin/theme-editor.php", data=post_data, timeout=30)
    print("Updated functions.php:", "File edited successfully" in r_up.text or "file-edited-successfully" in r_up.url)
else:
    print("Could not find old_ob_block in functions.php")

