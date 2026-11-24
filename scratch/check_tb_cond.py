from inspect_site import session
import re

admin_res = session.get("https://boloupgo.app/wp-admin/")
nonce = re.search(r'"nonce":"([^"]+)"', admin_res.text).group(1)
headers = {'X-WP-Nonce': nonce}

# Check options or elementor-pro theme builder
# In WordPress, let's see how Theme Builder conditions are stored
# In hello-elementor/functions.php we can read get_option('elementor_pro_theme_builder_conditions')
test_snippet = """
add_action('init', function() {
    if (isset($_GET['check_tb_conditions'])) {
        $conditions = get_option('elementor_pro_theme_builder_conditions', 'NOT_FOUND');
        header('Content-Type: application/json');
        echo json_encode(array(
            'option_conditions' => $conditions,
            'header_meta' => get_post_meta(32),
            'footer_meta' => get_post_meta(33)
        ));
        exit;
    }
});
"""

r_check = session.get("https://boloupgo.app/?check_tb_conditions=1")
print("Response status:", r_check.status_code)
print("Response text:", r_check.text[:500])

