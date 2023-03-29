function addprovedor() {
    const poNombre_proveedor = document.getElementById('nombreprovider');
    const poTelefono = document.getElementById('telprovider');
    const poDireccion = document.getElementById('dirreccionprovider');
    const poDescripcion = document.getElementById('telprovider');
   

    axios.post('guardarprovider', {
        
        Nombre_proveedor: poNombre_proveedor,
        Telefono: poTelefono.value,
        Direccion: poDireccion.value,
        Descripcion: poDescripcion.value
        

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