function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor').value;
    const nameinstructor = document.getElementById('nombreinstructor').value;
    const apeinstructor = document.getElementById('apellidoinstructor').value;
    const full = nameinstructor+ "" + apeinstructor;
    const telinstructor = document.getElementById('celinstructor').value;
    const espeinstructor = document.getElementById('espeinstruc').value;
    const usernameintruc = document.getElementById('usernameinstructor').value;
    const turnoinstruc = document.getElementById('jornadainstruc').value;    
    const passintruc = document.getElementById('passinstructor').value;
    const passinstruc = document.getElementById('passinstructor2').value;
    console.log(passinstruc, ccinstructor, nameinstructor,apeinstructor, telinstructor, full,espeinstructor, usernameintruc, turnoinstruc, passinstruc, passintruc);
   
    axios.post('saveinstructor', {
        full_name: full,
        Email: usernameintruc,
        telefono: telinstructor,
        especialidad: espeinstructor,
        jornada: turnoinstruc,
        id_roles: 2,
        cedula: ccinstructor,
        password: passintruc
        
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
    })
    .catch((err) => {
        console.log(err);
    })
}