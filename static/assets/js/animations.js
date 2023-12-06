document.addEventListener("DOMContentLoaded", function () {
    fill_progress_bar("js-stat__value--hp", "#30a7d7");
    fill_progress_bar("js-stat__value--attack", "#30a7d7");
    fill_progress_bar("js-stat__value--defense", "#30a7d7");
    fill_progress_bar("js-stat__value--special-attack", "#30a7d7");
    fill_progress_bar("js-stat__value--special-defense", "#30a7d7");
    fill_progress_bar("js-stat__value--speed", "#30a7d7");
    // Agregar un evento de clic al botón para cambiar la imagen
    document.getElementById('js-change-image').addEventListener('click', change_image);

});

function fill_progress_bar(id, color) {
    let totalId = "#" + id;
    let progressBarElement = document.querySelector(totalId);
    if (!progressBarElement) {
        return false;
    }
    let percentage = parseFloat(progressBarElement.getAttribute('data-value')) || 0;
    // Crear la barra de progreso
    let barra = new ProgressBar.Line(totalId, {
        strokeWidth: 4,
        easing: 'easeInOut',
        duration: 1500,
        color: color, // Usa el color pasado como parámetro
        trailColor: 'transparent', // Sin fondo de la barra
        trailWidth: 0, // Sin fondo de la barra
    });
    setTimeout(function () {
        barra.animate(percentage / 250);
    }, 1000);
}

// Asegúrate de incluir la biblioteca anime.js en tu proyecto

// Función para cambiar la imagen con una animación
function change_image() {
    const elementImage = document.getElementById('main-image');
    const buttonElement = document.getElementById('js-change-image');

    // Obtener los valores de las imágenes desde los atributos data
    const mainImage = elementImage.getAttribute('data-image-main');
    const shinyImage = elementImage.getAttribute('data-image-shiny');

    // Obtener el estado actual del botón
    const currentSateImage = parseInt(buttonElement.getAttribute('data-image-state'));


    // Cambiar la imagen y actualizar el estado
    anime({
        targets: elementImage,
        opacity: 0,
        duration: 500,
        easing: 'easeInOutQuad',
        complete: function () {
            // Cambiar la imagen después de la animación
            elementImage.src = currentSateImage === 1 ? mainImage : shinyImage;
            // Cambiar texto del botón después de la animación
            buttonElement.textContent = currentSateImage === 1 ? "shiny" : "volver";

            // Reiniciar la opacidad
            anime({
                targets: elementImage,
                opacity: 1,
                duration: 500,
                easing: 'easeInOutQuad'
            });

            // Actualizar el estado
            buttonElement.setAttribute('data-image-state', currentSateImage === 1 ? '2' : '1');
        }
    });
}


