document.addEventListener("DOMContentLoaded", function () {
    mostrarlibros()
});
function mostrarlibros() {
    /*const seltitulibro = document.getElementById('titu');
    const selautorlibro = document.getElementById('autores');
    const selyearlibro = document.getElementById('año');
    // Hacer una petición para un usuario con ID especifico
    axios.get('/api/libros')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            for (items in data) {
               let title = data[items].titulo
               let autor = data[items].id_autor
               let year = data[items].ano_publicado
                seltitulibro.innerHTML += (title);
                selautorlibro.innerHTML += (autor);
                selyearlibro.innerHTML += year;

            }
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });*/

    /*axios.get('/api/libros')
        .then(function (response) {
            // manejar respuesta exitosa
            // Obtener los datos de la base de datos
            const datos = response.data
            // Seleccionar el contenedor principal
            const contenedor = document.querySelector(".container-fluid");
            datos.forEach(dato => {
                // Crear un nuevo elemento de medios
                const nuevoElemento = document.createElement("div");
                nuevoElemento.classList.add("media", "media-hover");
                // Agregar la imagen
                const nuevaImagen = document.createElement("img");
                nuevaImagen.classList.add("media-object");
                nuevaImagen.src = "{{url_for('static', filename='assets/img/checklist.png')}}";
                nuevaImagen.alt = "Libro";
                nuevaImagen.width = "48";
                nuevaImagen.height = "48";
                const nuevoEnlace = document.createElement("a");
                nuevoEnlace.classList.add("tooltips-general");
                nuevoEnlace.href = "#!";
                nuevoEnlace.setAttribute("data-toggle", "tooltip");
                nuevoEnlace.setAttribute("data-placement", "right");
                nuevoEnlace.title = "Más información del libro";
                nuevoEnlace.appendChild(nuevaImagen);
                const nuevoMediaLeft = document.createElement("div");
                nuevoMediaLeft.classList.add("media-left", "media-middle");
                nuevoMediaLeft.appendChild(nuevoEnlace);
                nuevoElemento.appendChild(nuevoMediaLeft);
                console.log(nuevaImagen);
                console.log(nuevoEnlace);
                console.log(nuevoMediaLeft);

                // Agregar el título
                const nuevoTitulo = document.createElement("h4");
                nuevoTitulo.classList.add("media-heading");
                nuevoTitulo.style.fontSize = "22px";
                nuevoTitulo.textContent = dato.titulo;
                console.log(nuevoTitulo);

                // Agregar la información del autor y año
                const nuevoAutor = document.createElement("strong");
                nuevoAutor.id = "autores";
                nuevoAutor.textContent = dato.id_autor;
                console.log(nuevoAutor);
                const nuevoAño = document.createElement("strong");
                nuevoAño.id = "año";
                nuevoAño.textContent = dato.ano_publicado;
                console.log(nuevoAño);
                const nuevaInfo = document.createElement("div");
                nuevaInfo.classList.add("pull-left");
                nuevaInfo.appendChild(nuevoAutor);
                nuevaInfo.appendChild(document.createElement("br"));
                contenedor.appendChild(nuevoElemento)
            });
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });*/
}