function replaceWithIcon(imgElement) {
    // Obtenemos el contenedor de la imagen
    const parentContainer = document.getElementById('user-avatar-container');
    if (parentContainer) {
        // Creamos el nuevo elemento de icono
        const iconElement = document.createElement('i');
        iconElement.className = 'fa fa-user';

        // Reemplazamos la imagen que falló por el nuevo icono
        parentContainer.replaceChild(iconElement, imgElement);

        // Evitamos un bucle infinito si el icono también falla
        imgElement.onerror = null;
    }
}

// --- Autocompletado ---
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search-input");
    const suggestionsBox = document.getElementById("suggestions");

    searchInput.addEventListener("input", function() {
        const query = this.value;
        if (query.length < 2) {
            suggestionsBox.classList.add("hidden");
            return;
        }

        fetch(`/autocomplete/?q=${encodeURIComponent(query)}`)
            .then(response => response.json())
            .then(data => {
                suggestionsBox.innerHTML = "";
                if (data.length === 0) {
                    suggestionsBox.classList.add("hidden");
                    return;
                }

                data.forEach(title => {
                    const option = document.createElement("div");
                    option.classList.add(
                        'px-4', 'py-2', 'cursor-pointer',
                        'hover:bg-accent-blue', 'hover:text-white',
                        'bg-light-morado', 'text-text-light'
                    );
                    option.textContent = title;
                    option.addEventListener("click", function() {
                        searchInput.value = title;
                        suggestionsBox.classList.add("hidden");
                        searchInput.form.submit();
                    });
                    suggestionsBox.appendChild(option);
                });
                suggestionsBox.classList.remove("hidden");
            });
    });

    document.addEventListener("click", function(e) {
        if (!suggestionsBox.contains(e.target) && e.target !== searchInput) {
            suggestionsBox.classList.add("hidden");
        }
    });
});
