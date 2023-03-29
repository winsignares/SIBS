function Guardarlibros() {
    const titulobook = document.getElementById('titulolibro');
    const paisbook = document.getElementById('paislibro');
    const ano_publicadobook = document.getElementById('yearlibro');
    const copiasbook = document.getElementById('titulolibro');
    const estadobook = document.getElementById('estadolibro');
    const ubicacionbook = document.getElementById('ubicacionlibro');
    const id_deta_catbook = document.getElementById('titulolibro');
    const id_autorbook = document.getElementById('titulolibro');
    const id_editorialbook = document.getElementById('titulolibro');
    const id_proovbook = document.getElementById('titulolibro');

    alert(titulobook.value + paisbook.value + ano_publicadobook.value + copiasbook.value + estadobook.value + ubicacionbook.value + id_deta_catbook.value + id_autorbook.value + id_editorialbook.value + id_proovbook.value);
    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    /*axios.post('guardarbook', {
        titulo: titulobook.value,
        pais: paisbook.value,
        ano_publicado: ano_publicadobook.value,
        copias: copiasbook.value,
        estado: estadobook.value,
        ubicacion: ubicacionbook.value,
        id_deta_cat: id_deta_catbook.value,
        id_autor: id_autorbook.value,
        id_editorial: id_editorialbook.value,
        id_proov: id_proovbook.value
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
    })*/
}

function mostrarcategoriabook() {
    
    axios.get('libros', {

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

function mostrarproveedorbook() {
    alert("Hola");
}