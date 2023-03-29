const divestudiante = document.getElementById('reemplazable');

function listaestudiantes() {
    axios.get('/conliststudiantes', {
            responseType: 'json'
        })
        .then(function(response) {
            const datos = response.data
            let estudiante = '';
            for (let NIE in datos) {
                estudiante += `<div class="table-responsive">
                    <div class="div-table" style="margin:0 !important;">
                        <div class="div-table-row div-table-row-list">
                            <div class="div-table-cell" style="width: 6%;">#</div>
                            <div class="div-table-cell" style="width: 18%;">${NIE}</div>
                            <div class="div-table-cell" style="width: 18%;">${datos.full_name}</div>
                            <div class="div-table-cell" style="width: 18%;">${datos.Seccion}</div>
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
            divestudiante.innerHTML = estudiante
        })
        .catch(function(err) {
            console.log(err);
        })
        .then(function() {});
}