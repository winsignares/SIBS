const morfismo = document.getElementById('poli');
const i = 0;
window.onload = function viewpersonal() {
    axios.get('/conlistpersonal', {
            responseType: 'json'
        })
        .then(function(response) {
            const datos = response.data
            let listper = '';
            
            for (let DUI in datos) {
                i += 1
                listper += `<div class="table-responsive">
                    <div class="div-table" style="margin:0 !important;">
                        <div class="div-table-row div-table-row-list">
                        <div class="div-table-cell" style="width: 6%;">#</div>
                        <div id = "${i}" class="div-table-cell" style="width: 15%;">${DUI}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos.Nombre}</div>
                        <div class="div-table-cell" style="width: 12%;">${datos.Telefono}</div>
                        <div class="div-table-cell" style="width: 15%;">${datos.Cargo}</div>
                        <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-success"><i class="zmdi zmdi-refresh"></i></button>
                            </div>
                            <div class="div-table-cell" style="width: 9%;">
                                <button class="btn btn-danger"><i class="zmdi zmdi-delete"></i></button>
                            </div>
                        </div>
                    </div>
                </div>`;
            }
            morfismo.innerHTML = listper
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}

function eliminarpersonal(){
    const nose = document.getElementById('${i}');
    //const id = nose.textContent;
    axios.post('eliminarpersonal',{
        id: nose.textContent, 
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