function Guardarproveedor() {
    const Nombre_proveedor = document.getElementById('nombreprovider');
    const Telefono = document.getElementById('telprovider');
    const Direccion = document.getElementById('dirreccionprovider');
    const Descripcion = document.getElementById('telprovider');
   

    axios.post('guardarpro', {
        Nombre_proveedor: Nombre_proveedor,
        Telefono: Telefono,
        Direccion: Direccion,
        Descripcion: Descripcion,
        

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