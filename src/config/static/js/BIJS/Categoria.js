function GuardarCategoria() {
    const id = document.getElementById('codcategory');
    const N_cat = document.getElementById('name');
    const Descripcion = document.getElementById('description');



    axios.post('guardarcat', {
            id: id.value,
            N_cat: N_cat.value,
            Descripcion: Descripcion.value,


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

function mostrar() {
    alert("Hola");
}