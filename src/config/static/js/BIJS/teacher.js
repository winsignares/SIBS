function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor');
    const nameinstructor = document.getElementById('nombreinstructor');
    const apeinstructor = document.getElementById('apellidoinstructor');
    const telinstructor = document.getElementById('celinstructor');
    const espeinstructor = document.getElementById('espeinstruc');
    const usernameintruc = document.getElementById('usernameinstructor');
    const turnoinstruc = document.getElementById('jornadainstruc');    
    const secinstruc = document.getElementById('seccioninstruc');
    const passintruc = document.getElementById('passinstructor');
    const passinstruc = document.getElementById('passinstructor2');

    axios.post('guardaradmin', {
        fullname: nameinstructor.value,
        Email: emailadmin.value,
        Telefono: telinstructor.value,
        Especialidad: espeinstructor.value,
        Jornada: turnoinstruc.value        
       
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