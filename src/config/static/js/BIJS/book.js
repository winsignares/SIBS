function Guardarlibros() {
    const titulobook = document.getElementById('titulolibro');
    const paisbook = document.getElementById('titulolibro');
    const ano_publicadobook = document.getElementById('titulolibro');
    const copiasbook = document.getElementById('titulolibro');
    const estadobook = document.getElementById('titulolibro');
    const ubicacionbook = document.getElementById('titulolibro');
    const id_deta_catbook = document.getElementById('titulolibro');
    const id_autorbook = document.getElementById('titulolibro');
    const id_editorialbook = document.getElementById('titulolibro');
    const id_proovbook = document.getElementById('titulolibro');

    //alert(titlebook.value);
    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarbook', {
        titulo: titulobook.value,
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