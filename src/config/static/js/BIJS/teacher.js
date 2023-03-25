function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor');
    const nameinstructor = document.getElementById('nombreinstructor');
    const apeinstructor = document.getElementById('apellidoinstructor');
    const telinstructor = document.getElementById('celinstructor');
    const espeinstructor = document.getElementById('espeinstruc');
    const usernameintruc = document.getElementById('usernameinstructor');
    const passintruc = document.getElementById('passinstructor');
    const passinstruc = document.getElementById('passinstructor2');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardaradmin', {
        fullname: nameinstructor.value,
        Email: emailadmin.value,
        Telefono: telinstructor.value,
        Especialidad: espeinstructor.value,        
        //orders: [1, 2, 3],
        //photo: document.querySelector('#fileInput').files
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