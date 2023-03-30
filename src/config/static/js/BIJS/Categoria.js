function GuardarCategoria() {
    const N_cat = document.getElementById('name');
    const Descripcion = document.getElementById('description');

    axios.post('guardarcategoria', {
            NumeroCategoria: N_cat.value,
            descripcion: Descripcion.value
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