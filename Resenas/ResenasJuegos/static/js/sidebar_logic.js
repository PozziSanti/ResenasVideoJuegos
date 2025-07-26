document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    let isSidebarOpen = false; // El sidebar comienza cerrado por defecto

    // Función para alternar el estado del sidebar
    function toggleSidebar() {
        isSidebarOpen = !isSidebarOpen;
        updateSidebarState();
    }

    // Función para actualizar el estado del sidebar
    function updateSidebarState() {
        if (isSidebarOpen) {
            sidebar.classList.remove('-translate-x-full'); // Muestra el sidebar
            sidebar.classList.add('translate-x-0');
        } else {
            sidebar.classList.remove('translate-x-0'); // Oculta el sidebar
            sidebar.classList.add('-translate-x-full');
        }
        // Ya no necesitamos modificar mainContentWrapper.classList
    }

    // Manejar click en el botón de menú
    if (menuToggle) { // Asegúrate de que el botón exista antes de agregar el listener
        menuToggle.addEventListener('click', toggleSidebar);
    }

    // Ajustar el sidebar al cambiar el tamaño de la ventana (para responsividad)
    // Ya no es necesario que JavaScript maneje las propiedades fixed, top, h-full, w-64, z-40
    // Estas clases las dejamos directamente en el HTML del sidebar.
    // Solo necesitamos asegurarnos de que el estado inicial se aplique.
    window.addEventListener('resize', function () {
        // En todas las resoluciones, el sidebar actúa como overlay
        // No hay necesidad de añadir/quitar estas clases aquí, ya están en HTML
        // sidebar.classList.add('fixed', 'left-0', 'top-16', 'h-[calc(100vh-4rem)]', 'w-64', 'z-40', 'transition-transform', 'duration-300', 'ease-in-out');

        // La clase `lg:hidden` en el botón del menú en el header ya maneja su visibilidad.
        // Las clases de `lg:` en el sidebar ya no lo hacen parte del flujo.
        // Simplemente aseguramos que el estado visual del sidebar sea consistente.
        updateSidebarState();
    });

    // Llamada inicial para establecer el estado del sidebar al cargar la página
    // Esto asegura que el sidebar esté inicialmente oculto si isSidebarOpen es false.
    updateSidebarState(); // Llama directamente, no dispares un evento 'resize' innecesario.
});