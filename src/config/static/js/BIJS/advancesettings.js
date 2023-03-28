//Eliminar libros
function Eliminarlibro() {
    Swal.fire({
        icon: 'warning',
        html:
        'ingrese el id que desea eliminar'    +  
        '<input id="id_instructor" class="swal2-input">', 
    })
}
//Eliminar aprendiz
function EliminarEstudiantes() {
    Swal.fire({
        title: 'Eliminar Estudiantes',
        input: 'select',
        icon: 'warning',
        showCancelButton: true,
        inputOptions: {
            'Rol': {
                Roles: 'Elige',
                Aprendiz: 'Aprendiz'
            },
        },
        html:
        'ingrese el id que desea eliminar'    +  
        '<input id="id_instructor" class="swal2-input">',

    }) 
};


//Eliminar Instructor
function EliminarDocente() {
    Swal.fire({
        title: 'Eliminar Instructor',
        input: 'select',
        icon: 'warning',
        showCancelButton: true,
        inputOptions: {
            'Rol': {
                Roles: 'Elige',
                Instructor: 'Instructor'
            },
        },
        html:
        'ingrese el id que desea eliminar'    +  
        '<input id="id_instructor" class="swal2-input">',
    })
};
// funcion eliminar bitacora
function EliminarBitacora(){
    Swal.fire({
        title: 'desea eliminar la bitacora',
        text: 'al momento de borrarse los datos no podran recuperarse',
        confirmButtonText: 'confirmar',
        showCancelButton: true,
        icon: 'warning'

    })
};

function EliminarPadministrativo() {
    Swal.fire({
        title: 'Eliminar Personal Administrativo',
        input: 'select',
        icon: 'warning',
        showCancelButton: true,
        inputOptions: {
            'Rol': {
                Roles: 'Elige',
                Personal_Administrativo: 'Personal Administrativo'
            },
        },
        html:
        'ingrese el id que desea eliminar'    +  
        '<input id="id_instructor" class="swal2-input">',
    })
}