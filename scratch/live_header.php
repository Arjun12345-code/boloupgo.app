<?php
/**
 * The template for displaying the header
 *
 * @package HelloElementor
 */
if ( ! defined( 'ABSPATH' ) ) {
	exit; // Exit if accessed directly.
}

$viewport_content = apply_filters( 'hello_elementor_viewport_content', 'width=device-width, initial-scale=1' );
?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="<?php echo esc_attr( $viewport_content ); ?>">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	<link rel="stylesheet" href="/style.css">
		<link rel="icon" type="image/png" sizes="32x32" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-150x150.png">
	<link rel="icon" type="image/png" sizes="192x192" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png">
	<link rel="apple-touch-icon" href="https://boloupgo.app/wp-content/uploads/2026/11/cropped-boloup-300x300.png">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- ==========================================================================
     BoloUp Go Official - Header Component (header.html)
     For WordPress Elementor Theme Builder Header Template
     ========================================================================== -->
<header class="header" id="header">
  <div class="header-container">
    <a href="/" class="brand-logo" id="brand-logo" aria-label="BoloUp Go Official Home">
      <img src="https://boloupgo.app/wp-content/uploads/2026/11/logo-samping.png" alt="BoloUp Go Official Logo"
        class="brand-logo-icon" width="914" height="261">
    </a>

    <nav class="nav-menu" id="nav-menu" aria-label="Main Navigation">
      <a href="/" class="nav-link" id="nav-home">Home</a>
      <a href="/host" class="nav-link" id="nav-host">Host</a>
      <a href="/agent" class="nav-link" id="nav-agent">Agent</a>
      <a href="/contact" class="nav-link" id="nav-contact">Contact</a>
      <div class="mobile-nav-actions">
        <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-outline" id="btn-mobile-download">Download App</a>
        <a href="/host" class="btn btn-primary" id="btn-mobile-host">Become a Host</a>
      </div>
    </nav>

    <div class="header-actions">
      <a href="https://share.bololinks.com/home/scode/47282" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm" id="btn-header-download">Download App</a>
      <a href="/host" class="btn btn-primary btn-sm" id="btn-header-host">Become a Host</a>
      <button type="button" class="menu-toggle" id="menu-toggle" aria-label="Toggle Navigation Menu" aria-expanded="false" aria-controls="nav-menu">&#9776;</button>
    </div>
  </div>
</header>

<script>
  (function () {
    // Set background to deep dark
    document.documentElement.style.setProperty('background-color', '#080718', 'important');
    if (document.body) {
      document.body.style.setProperty('background-color', '#080718', 'important');
    }

    const menuToggle = document.getElementById('menu-toggle');
    const navMenu = document.getElementById('nav-menu');
    if (menuToggle && navMenu) {
      function toggleMenu(open) {
        const shouldOpen = open !== undefined ? open : !navMenu.classList.contains('active');
        navMenu.classList.toggle('active', shouldOpen);
        menuToggle.textContent = shouldOpen ? '✕' : '☰';
        menuToggle.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
      }

      menuToggle.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleMenu();
      });

      // Close menu when clicking outside
      document.addEventListener('click', function (e) {
        if (!navMenu.contains(e.target) && !menuToggle.contains(e.target)) {
          toggleMenu(false);
        }
      });

      // Close menu when a link inside is clicked
      navMenu.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          toggleMenu(false);
        });
      });

      // Close on Escape key
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && navMenu.classList.contains('active')) {
          toggleMenu(false);
        }
      });
    }

    // Highlight current page active link
    const currentPath = window.location.pathname.replace(/\/+$/, '') || '/';
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function (link) {
      const href = (link.getAttribute('href') || '').replace(/\/+$/, '') || '/';
      if (href === currentPath || (href === '/' && (currentPath === '' || currentPath === '/index.html'))) {
        link.classList.add('active');
      }
    });

    // Fixed Header Lock & Elementor parent container cleanup
    const header = document.getElementById('header');
    if (header) {
      function lockHeaderPosition() {
        header.style.setProperty('position', 'fixed', 'important');
        header.style.setProperty('top', '0px', 'important');
        header.style.setProperty('left', '0px', 'important');
        header.style.setProperty('right', '0px', 'important');
        header.style.setProperty('width', '100%', 'important');
        header.style.setProperty('z-index', '99999', 'important');

        // Check if WordPress admin bar is present and offset top
        const wpAdminBar = document.getElementById('wpadminbar');
        if (wpAdminBar) {
          const barHeight = wpAdminBar.offsetHeight || 32;
          header.style.setProperty('top', barHeight + 'px', 'important');
        }
      }

      window.addEventListener('scroll', lockHeaderPosition, { passive: true });
      window.addEventListener('resize', lockHeaderPosition);
      document.addEventListener('DOMContentLoaded', lockHeaderPosition);
      lockHeaderPosition();
    }
  })();
</script>

