document.addEventListener("DOMContentLoaded", function () {
    mostrarlibros()
});

function mostrarlibros() {
    const seltitulibro = document.getElementById('titu');
    const selautorlibro = document.getElementById('autores');
    const selyearlibro = document.getElementById('año');
    // Hacer una petición para un usuario con ID especifico
    axios.get('/api/libros')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            data.forEach(dato => {
               let title = dato.titulo
               let autor = dato.id_autor
               let year = dato.ano_publicado
                seltitulibro.innerHTML = (title);
                selautorlibro.innerHTML = (autor);
                selyearlibro.innerHTML = year;

            });
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });

    /*axios.get('/api/libros')
        .then(function (response) {
            // manejar respuesta exitosa
            // Obtener los datos de la base de datos
            const datos = response.data
            // Seleccionar el contenedor principal
            const contenedor = document.getElementById("contendorcatalogo");
            datos.forEach(dato => {
                titulolibro = dato.titulo
                autorlibro = dato.id_autor
                yearlibro = dato.ano_publicado

                divgeneral = `        <div class="media media-hover">
                <div class="media-left media-middle">
                    <a href="#!" class="tooltips-general" data-toggle="tooltip" data-placement="right"
                        title="Más información del libro">
                        <img class="media-object" src="{{url_for('static', filename='assets/img/book.png')}}" alt="Libro"
                            width="48" height="48">
                    </a>
                </div>
                <div class="media-body">
                    <h4 class="media-heading"  id="titu">${titulolibro}</h4>
                    <div class="pull-left">
                        <strong id="autores">${autorlibro}</strong><br>
                            <strong id="año">${yearlibro}</strong>
                    </div>
                    <p class="text-center pull-right">
                        <a  class="modal_button"  href="#!" class="btn btn-info btn-xs" style="margin-right: 10px;"><i
                                class="zmdi zmdi-info-outline"></i> &nbsp;&nbsp; Más información</a>
                    </p>
                </div>
            </div>
            <!--MODAL-->
            <section class="modal1">
                <div class="modal-container">
                    <h2>¡Mas informacion de el libro escogido!</h2>
                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Consequuntur quo dicta minus ipsum,
                        deserunt quas dolorem sunt architecto cum, omnis cumque officiis voluptatum ab laborum, aperiam
                        nesciunt illo totam ea?</p>
                    <div class="close_Modal">x</div>
                </div>
            </section>
        </div>
        <!--FINAL MODAL-->`
                contenedor.innerHTML += (divgeneral);
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