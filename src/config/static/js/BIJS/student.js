function GuardarStudent() {
    const ccestudiante = document.getElementById('idestudiante');
    const nameestudiante = document.getElementById('nombreestudiante');
    const apeestudiante = document.getElementById('apellidoestudiante');
    const formaestudiante = document.getElementById('formaestudiante');
    const numccinstructorencar = document.getElementById('numccinstructorencargado');  
    const fullnameinstructor = document.getElementById('fullnameinstructor');
    const generoestudiante = document.getElementById('generoestudiante');
    const telestudiante = document.getElementById('telestudiante');
    const nomusuarioestudiante = document.getElementById('nomusuarioestudiante');
    const contraseña = document.getElementById('contraseña');
    const repcontraseña = document.getElementById('repcontraseña');
    
    
    
    axios.post('guarstudent', {
        ccestudiante: ccestudiante.value,
        fullname: nameestudiante.value,
        Apellido: apeestudiante.value,
        formaestudiante: formaestudiante.value,
        numccinstructorencar: numccinstructorencar.value,
        fullnameinstructor: fullnameinstructor.value,
        generoestudiante: generoestudiante.value,
        Telefono: telestudiante.value,
        nomusuarioestudiante: nomusuarioestudiante.value,
        contraseña: contraseña.value,
        repcontraseña: repcontraseña.value
       
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
function limpiarStudent() {
    const ccestudiante = document.getElementById('idestudiante');
    const nameestudiante = document.getElementById('nombreestudiante');
    const apeestudiante = document.getElementById('apellidoestudiante');
    const formaestudiante = document.getElementById('formaestudiante');
    const numccinstructorencar = document.getElementById('numccinstructorencargado');  
    const fullnameinstructor = document.getElementById('fullnameinstructor');
    const generoestudiante = document.getElementById('generoestudiante');
    const telestudiante = document.getElementById('telestudiante');
    const nomusuarioestudiante = document.getElementById('nomusuarioestudiante');
    const contraseña = document.getElementById('contraseña');
    const repcontraseña = document.getElementById('repcontraseña');

    /*no se que es esto*/
    ccestudiante.value ="";
    nameestudiante.value ="";
    apeestudiante.value ="";
    formaestudiante.value ="";
    numccinstructorencar.value ="";
    fullnameinstructor.value ="";
    generoestudiante.value ="";
    telestudiante.value ="";
    nomusuarioestudiante.value ="";
    contraseña.value ="";
    repcontraseña.value ="";
}
