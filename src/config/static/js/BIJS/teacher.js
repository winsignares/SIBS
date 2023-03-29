function GuardarInstructor() {
    const ccinstructor = document.getElementById('idinstructor');
    const nameinstructor = document.getElementById('nombreinstructor');
    const apeinstructor = document.getElementById('apellidoinstructor');
    const full = nameinstructor+ "" + apeinstructor;
    const telinstructor = document.getElementById('celinstructor');
    const espeinstructor = document.getElementById('espeinstruc');
    const usernameintruc = document.getElementById('usernameinstructor');
    const turnoinstruc = document.getElementById('jornadainstruc');    
    const passintruc = document.getElementById('passinstructor');
    const passinstruc = document.getElementById('passinstructor2');
   
    axios.post('saveinstructor', {
        full_name: full.value,
        password: passintruc.value,
        Email: usernameintruc.value,
        telefono: telinstructor.value,
        especialidad: espeinstructor.value,
        jornada: turnoinstruc.value,
        id_roles: 4,        
        Cedula: ccinstructor.value       
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