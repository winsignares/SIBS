function GuardarAdministrador() {
    const nameadmin = document.getElementById('nombreadmin');
    const emailadmin = document.getElementById('emailadmin');
    const usernameadmin = document.getElementById('usernameadmin');
    const passadmin = document.getElementById('passadmin');
    const passadmin2 = document.getElementById('passadmin2');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${nameadmin.value} ${emailadmin.value}${usernameadmin.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardaradmin', {
        fullname: nameadmin.value,
        Email: emailadmin.value
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

swal("Confirmar!", "You clicked the button!", {
	icon : "warning",
	buttons: {
		confirm: {
			className : 'btn btn-warning'
		}
	},
});

swal("Good job!", "You clicked the button!", {
	icon : "error",
	buttons: {
		confirm: {
			className : 'btn btn-danger'
		}
	},
});

swal("Good job!", "You clicked the button!", {
	icon : "success",
	buttons: {
		confirm: {
			className : 'btn btn-success'
		}
	},
});

swal("Good job!", "You clicked the button!", {
	icon : "info",
	buttons: {
		confirm: {
			className : 'btn btn-info'
		}
	},
});