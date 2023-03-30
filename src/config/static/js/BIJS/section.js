//----------------------------------------------------------------
function addSection() {
    const OpYear = document.getElementById('getOptionYear').value;
    const OpEspecialidad = document.getElementById('getOptionEspecialidad').value;
    const OpSeccion = document.getElementById('getOptionSeccion').value;
<<<<<<< HEAD
    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${Inputname.value} ${emailadmin.value}${userInputname.value} ${passadmin.value}`): alert('los campos son diferentes');
=======

>>>>>>> main
    axios.post('guardarsection', {
            year: OpYear,
            especialidad: OpEspecialidad,
            seccion: OpSeccion


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