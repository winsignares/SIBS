function addTbl() {
    const addtable = document.getElementById('addTableSeccion');
    //Traer los datos de la BD y colocarlos en las tablas

    axios.get('showsection', {
            year: OpYear,
            especialidad: OpEspecialidad
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
    var tb = `<div class="div-table-row">
    <div class="div-table-cell">#</div>
    <div class="div-table-cell">Nombre</div>
    <div class="div-table-cell">
        <button class="btn btn-danger btn-xs"><i class="zmdi zmdi-delete"></i> &nbsp;&nbsp; Eliminar</button>
    </div>
    </div>`

    addtable.innerHTML = tb;
}