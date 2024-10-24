// Función para cambiar el color de fondo al pasar el mouse por los géneros
const peliculas = document.querySelectorAll('.pelicula');

peliculas.forEach(pelicula => {
    const generoList = pelicula.querySelectorAll('ul li');

    generoList.forEach(genero => {
        genero.addEventListener('mouseover', () => {
            // Cambia el color de fondo de la película según el género
            const generoTexto = genero.textContent.toLowerCase();
            if (generoTexto.includes('acción')) {
                pelicula.style.backgroundColor = '#FF7043'; // Naranja para Acción
            } else if (generoTexto.includes('ciencia ficción')) {
                pelicula.style.backgroundColor = '#29B6F6'; // Azul claro para Ciencia Ficción
            } else if (generoTexto.includes('aventura')) {
                pelicula.style.backgroundColor = '#66BB6A'; // Verde para Aventura
            } else {
                pelicula.style.backgroundColor = '#E0E0E0'; // Gris claro por defecto
            }
        });

        genero.addEventListener('mouseout', () => {
            // Restaura el color original al salir del mouse
            pelicula.style.backgroundColor = '#E0E0E0'; // Gris claro original
        });
    });
});

// Función para cambiar el color del título principal con un botón
const cambiarColorTituloBtn = document.querySelector('#cambiarColorTitulo');
const tituloPrincipal = document.querySelector('h1');

cambiarColorTituloBtn.addEventListener('click', () => {
    // Genera un color aleatorio para el título
    const randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
    tituloPrincipal.style.color = randomColor;
    tituloPrincipal.style.transition = 'color 0.5s ease'; // Animación suave
});
document.addEventListener("DOMContentLoaded", function() {
    const darkModeButton = document.getElementById("darkModeToggle");
    
    darkModeButton.addEventListener("click", function() {
      document.body.classList.toggle("dark-mode");
    });
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    const darkModeButton = document.getElementById("darkModeToggle");
    const cambiarColorTituloButton = document.getElementById("cambiarColorTitulo");
    const titulo = document.querySelector("h1");
    const reseñasForm = document.querySelector("#reseñas form");
    const nombreInput = document.getElementById("nombre");
    const mensajeInput = document.getElementById("mensaje");

    // Modo Oscuro
    darkModeButton.addEventListener("click", function() {
        document.body.classList.toggle("dark-mode");
    });

    // Cambiar el color del título
    cambiarColorTituloButton.addEventListener("click", function() {
        titulo.classList.toggle("cambio-color");
    });

    // Enviar Reseña
    reseñasForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío del formulario
        const nombre = nombreInput.value.trim();
        const mensaje = mensajeInput.value.trim();

        if (nombre && mensaje) {
            alert(`¡Gracias por tu reseña, ${nombre}!`);
            // Limpiar los campos del formulario
            nombreInput.value = '';
            mensajeInput.value = '';
        } else {
            alert("Por favor completa todos los campos.");
        }
    });
});



