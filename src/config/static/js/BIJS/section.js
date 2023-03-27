//----------------------------------------------------------------
function GuardarSection() {
    const Inputname = document.getElementById('nombreadmin');
    const emailadmin = document.getElementById('emailadmin');
    const userInputname = document.getElementById('userInputname');
    const passadmin = document.getElementById('passadmin');
    const passadmin2 = document.getElementById('passadmin2');

    //passadmin.value === passadmin2.value ? alert(`Estos son los datos del administrador ${Inputname.value} ${emailadmin.value}${userInputname.value} ${passadmin.value}`): alert('los campos son diferentes');
    axios.post('guardaradmin', {
            fullname: Inputname.value,
            Email: emailadmin.value
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
/**
 * year
 */