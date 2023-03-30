function addprovedor() {
    const Nombre_proveedorr = document.getElementById('nombreprovider');
    const correoprovider = document.getElementById('emailprovider');
    const Direccionprovider = document.getElementById('dirreccionprovider');
    const telefonoprovider = document.getElementById('telprovider');
    const responsableprovider = document.getElementById('resprovider');
    
   alert('a')

    axios.post('guardarprovider', {
        
        Nombre_proveedor: Nombre_proveedorr.value,
        correo: correoprovider.value,
        Direccion: Direccionprovider.value,
        telefono: telefonoprovider.value,
        Descripcion: responsableprovider.value
        

    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }).then((res) => {
        console.log(res.data)
    })
    .catch((error) => {
        console.error(error)
    })
}