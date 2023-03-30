function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor').value;
    const nameinstructor = document.getElementById('nombreinstructor').value;
    const apeinstructor = document.getElementById('apellidoinstructor').value;
    const full = nameinstructor + apeinstructor;
    const telinstructor = document.getElementById('celinstructor').value;
    const espeinstructor = document.getElementById('espeinstruc').value;
    const usernameintruc = document.getElementById('usernameinstructor').value;
    const turnoinstruc = document.getElementById('jornadainstruc').value;    
    const secinstruc = document.getElementById('seccioninstruc').value;
    const passintruc = document.getElementById('passinstructor').value;
    const passinstruc = document.getElementById('passinstructor2'.value);

    axios.post('saveinstructor', {
        full_name: full,
        email: usernameintruc,
        telefono: telinstructor,
        especialidad: espeinstructor,
        Jornada: turnoinstruc,
        password: passintruc,
        Cedula: ccinstructor
       
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