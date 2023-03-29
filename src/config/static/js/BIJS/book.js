function Guardarlibros() {
    const titulobook = document.getElementById('titulolibro');
    const id_autorbook = document.getElementById('titulolibro');
    const paisbook = document.getElementById('paislibro');
    const id_Categoriabook = document.getElementById('titulolibro');
    const id_proveedorbook = document.getElementById('titulolibro');
    const ano_publicadobook = document.getElementById('yearlibro');
    const editorialbook = document.getElementById('titulolibro');
    const ubicacionbook = document.getElementById('ubicacionlibro');
    const estadobook = document.getElementById('estadolibro');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarbook', {
        titulo: titulobook.value,
        id_autor: id_autorbook.value,
        pais: paisbook.value,
        id_Categoria: id_Categoriabook.value,
        id_proveedor: id_proveedorbook.value,
        ano_publicado: ano_publicadobook.value,
        editorial: editorialbook.value,
        ubicacion: ubicacionbook.value,
        estado: estadobook.value
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)


    })
    .catch((error) => {
        console.error(error)
    })
}

function mostrarcategoriabook() {
}

function mostrarproveedorbook() {
}