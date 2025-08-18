// --- Avatar fallback ---
function replaceWithIcon(imgElement) {
    // Obtenemos el contenedor de la imagen
    const parentContainer = document.getElementById('user-avatar-container');
    if (!parentContainer) return;

    const icon = document.createElement('i');
    icon.className = 'fa fa-user';
    parent.replaceChild(icon, imgElement);

    // Evitamos un bucle infinito si el icono también falla
    imgElement.onerror = null;
}

document.addEventListener("DOMContentLoaded", function () {

    // --- Autocompletado buscador ---
    const searchInput = document.getElementById("search-input");
    const suggestionsBox = document.getElementById("suggestions");

    searchInput?.addEventListener("input", function () {
        const query = this.value;
        if (query.length < 2) {
            suggestionsBox.classList.add("hidden");
            return;
        }

        fetch(`/autocomplete/?q=${encodeURIComponent(query)}`)
            .then(res => res.json())
            .then(data => {
                suggestionsBox.innerHTML = "";
                if (!data.length) {
                    suggestionsBox.classList.add("hidden");
                    return;
                }

                data.forEach(title => {
                    const option = document.createElement("div");
                    option.className = 'px-4 py-2 cursor-pointer bg-light-morado text-text-light hover:bg-accent-blue hover:text-white';
                    option.textContent = title;
                    option.addEventListener("click", () => {
                        searchInput.value = title;
                        suggestionsBox.classList.add("hidden");
                        searchInput.form.submit();
                    });
                    suggestionsBox.appendChild(option);
                });

                suggestionsBox.classList.remove("hidden");
            });
    });

    document.addEventListener("click", e => {
        if (!suggestionsBox.contains(e.target) && e.target !== searchInput) {
            suggestionsBox.classList.add("hidden");
        }
    });

    // --- Menú hamburguesa ---
    const menuToggle = document.getElementById('menu-toggle');
    menuToggle?.addEventListener('click', () => {
        document.body.classList.toggle('overflow-hidden'); // bloquea scroll
        // Aquí abrís/cerrás tu sidebar;
    });

    // --- Dropdown filtros ---
    const filterToggle = document.getElementById('filters-toggle');
    const filterDropdown = document.getElementById('filters-dropdown');

    filterToggle?.addEventListener('click', (e) => {
        e.preventDefault();
        filterDropdown.classList.toggle('hidden');
    });

    // Cerrar dropdown si clickeas afuera
    document.addEventListener('click', (e) => {
        if (!filterToggle.contains(e.target) && !filterDropdown.contains(e.target)) {
            filterDropdown.classList.add('hidden');
        }
    });

});
