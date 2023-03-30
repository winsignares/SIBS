function GuardarCategoria() {
    const N_cat = document.getElementById('numero');
    const Descripcion = document.getElementById('name');

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