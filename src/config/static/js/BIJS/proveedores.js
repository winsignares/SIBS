function addprovedor() {
    const Nombre_proveedorr = document.getElementById('nombreprovider').value;
    const correoprovider = document.getElementById('emailprovider').value;
    const Direccionprovider = document.getElementById('dirreccionprovider').value;
    const telefonoprovider = document.getElementById('telprovider').value;
    const responsableprovider = document.getElementById('resprovider').value;
    


    axios.post('guardarprovider', {
        
        Nombre_proveedor: Nombre_proveedorr,
        correo: correoprovider,
        Direccion: Direccionprovider,
        telefono: telefonoprovider,
        Descripcion: responsableprovider
        

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