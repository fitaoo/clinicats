document.addEventListener('DOMContentLoaded', function () {
    console.log("Sitio activo, listo para deslizar anuncios 🎉");
});

document.addEventListener('DOMContentLoaded', function () {
    const lineas = document.querySelectorAll('#hero-heading .linea');
    lineas.forEach((linea, index) => {
        setTimeout(() => {
            linea.classList.add('visible');
        }, index * 800);
    });
});
