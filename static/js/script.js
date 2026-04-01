// VivaSim — script.js

// Auto-hide flash messages after 4 seconds
document.addEventListener('DOMContentLoaded', function () {
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(function (el) {
        setTimeout(function () {
            el.style.transition = 'opacity 0.5s';
            el.style.opacity = '0';
            setTimeout(function () { el.remove(); }, 500);
        }, 4000);
    });

    // Highlight active nav link based on current URL
    const links = document.querySelectorAll('.nav-link');
    links.forEach(function (link) {
        if (link.getAttribute('href') === window.location.pathname) {
            link.classList.add('active');
        }
    });
});
