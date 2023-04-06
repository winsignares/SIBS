$(function() {
    $("#yearlibro").datepicker({
    dateFormat: "yy",
    changeYear: true,
    yearRange: "-100:+0"
    });
  });

function Guardarlibros() {
    const titulobook = document.getElementById('titulolibro');
    const id_autorbook = document.getElementById('autorlibro');
    const paisbook = document.getElementById('paislibro');
    const id_Categoriabook = document.getElementById('categorialibro');
    const id_proveedorbook = document.getElementById('proveedorlibro');
    const ano_publicadobook = document.getElementById('yearlibro');
    const editorialbook = document.getElementById('editoriallibro');
    const ubicacionbook = document.getElementById('ubicacionlibro');
    const estimadobook = document.getElementById('estimadolibro');
    const cargobook = document.getElementById('cargobook');
    const estadobook = document.getElementById('estadolibro');

    axios.post('guardarbook', {
        titulo: titulobook.value,
        id_autor: id_autorbook.value,
        pais: paisbook.value,
        id_Categoria: id_Categoriabook.value,
        id_proveedor: id_proveedorbook.value,
        ano_publicado: ano_publicadobook.value,
        editorial: editorialbook.value,
        ubicacion: ubicacionbook.value,
        estimado: estimadobook.value,
        cargo: cargobook.value,
        estado: estadobook.value
    }, 
    {
        headers: {
            'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        document.getElementById("modal-message").textContent = "Información guardada exitosamente";
        $("#myModal").modal();
    })
        .catch((error) => {
            console.error(error)
            document.getElementById("modal-message").textContent = "No se pudo guardar la información. Por favor, verifica que los campos estén llenos correctamente.";
            $("#myModal").modal();
        })
}
// FUNCION PARA MOSTRAR LOS AUTORES
document.addEventListener("DOMContentLoaded", function () {
    mostrarautor()
    mostrarcategoria()
    mostrarproveedor()
});
function mostrarautor() {
    const selautorlibro = document.getElementById('autorlibro');
    // Hacer una petición para un usuario con ID especifico
    axios.get('/api/autores')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            for (items in data) {
                const opcion = document.createElement('option');
                opcion.value = data[items].id;
                opcion.text = data[items].nombre;
                selautorlibro.appendChild(opcion);
            }
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });
}
// FUNCION PARA MOSTRAR LOS AUTORES
function mostrarcategoria() {
    const selcategorialibro = document.getElementById('categorialibro');
    axios.get('mostrarCategorias')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            for (items in data) {
                const opcion = document.createElement('option');
                opcion.value = data[items].id;
                opcion.text = data[items].Nombre_categoria;
                selcategorialibro.appendChild(opcion);
            }
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });
}
// FUNCION PARA MOSTRAR LOS AUTORES
function mostrarproveedor() {
    const selproveedorlibro = document.getElementById('proveedorlibro');
    axios.get('/api/proveedores')
        .then(function (response) {
            // manejar respuesta exitosa
            console.log(response.data);
            const data = response.data
            for (items in data) {
                const opcion = document.createElement('option');
                opcion.value = data[items].id;
                opcion.text = data[items].Nombre_proveedor;
                selproveedorlibro.appendChild(opcion);
            }
        })
        .catch(function (error) {
            // manejar error
            console.log(error);
        })
        .finally(function () {
            // siempre sera executado
            console.log("Ejcucion Finalizada");
        });
}