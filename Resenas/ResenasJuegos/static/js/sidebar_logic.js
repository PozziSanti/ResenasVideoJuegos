document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    let isSidebarOpen = false; // Sidebar arranca cerrado

    function openSidebar() {
        sidebar.classList.remove('-translate-x-full');
        sidebar.classList.add('translate-x-0');
    }

    function closeSidebar() {
        sidebar.classList.remove('translate-x-0');
        sidebar.classList.add('-translate-x-full');
    }

    function toggleSidebar() {
        isSidebarOpen = !isSidebarOpen;
        isSidebarOpen ? openSidebar() : closeSidebar();
    }

    if (menuToggle) {
        menuToggle.addEventListener('click', toggleSidebar);
    }

    // Estado inicial -> sidebar cerrado
    closeSidebar();
});
