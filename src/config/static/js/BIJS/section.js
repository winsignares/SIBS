//----------------------------------------------------------------
function addSection() {
    const OpYear = document.getElementById('getOptionYear');
    const OpEspecialidad = document.getElementById('getOptionEspecialidad');
    const OpSeccion = document.getElementById('getOptionSeccion');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${Inputname.value} ${emailadmin.value}${userInputname.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardarsection', {
            year: OpYear.value,
            especialidad: OpEspecialidad.value,
            seccion: OpSeccion.value

            //orders: [1, 2, 3],
            //photo: document.querySelector('#fileInput').files
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