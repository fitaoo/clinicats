window.addEventListener("load", () => {
    const preloader = document.getElementById("preloader");
    if (preloader) {
        preloader.classList.add("fade-out");

        setTimeout(() => {
            preloader.remove();

            const clinica = document.querySelector('#hero-heading .clinica');
            const tierraSanta = document.querySelector('#hero-heading .tierra-santa');
            const subtitulo = document.getElementById('hero-subtitle');

            if (clinica) {
                clinica.classList.add('visible');
            }

            setTimeout(() => {
                if (tierraSanta) {
                    tierraSanta.classList.add('visible');
                }

                setTimeout(() => {
                    if (subtitulo) {
                        subtitulo.classList.add('visible');
                    }
                }, 1000); // aparece después de Tierra Santa

            }, 2000); // tiempo entre Clínica y Tierra Santa

        }, 1000); // duración del fade-out
    }
});


