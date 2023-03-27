function Guardarproveedor() {
    const nombreproveedor = document.getElementById('nombreprovider');
    const emailproveedor = document.getElementById('emailprovider');
    const dirreccionpro = document.getElementById('dirreccionprovider');
    const telefonopro = document.getElementById('telprovider');
    const responsable_atencion = document.getElementById('resprovider');

    axios.post('guardarprovee', {
        fullname: nombreproveedor.value,
        Email: emailproveedor.value,
        Dirreccion: dirreccionpro.value,
        Telefono: telefonopro.value,
        Responsable: responsable_atencion.value

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