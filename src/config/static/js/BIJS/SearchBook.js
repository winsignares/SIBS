<<<<<<< HEAD
const searchbook = 

document.getElementById("searchbook");
const list = 
document.getElementById("list");
const items = 
list.getElementsByTagName("li");

const searchFunction = () => {

    const searchText = 
    searchbook.Value.toLowerCase();
    for (let i= 0; i < items.length;i++)
    {const currentitem = items[i]}
    const itemText = 
    currentitem.innerText.toLowerCase();

    if (itemText.includes(searchText)){currentitem.style.display = "block";} 
    
    else {currentitem.style.display = "none";} 

}

searchbook.addEventListener("input",searchFunction);
=======
function buscar() {
    const query = document.getElementById('searchboock').value;
    // Realiza una búsqueda en base a la consulta del usuario
    // ...
    const results = []; // Los resultados son un arreglo de cadenas, pero podrían ser cualquier cosa (objetos, números, etc.)
    const resultList = document.getElementById('result-list');
    resultList.innerHTML = ''; // Limpia los resultados anteriores
    results.forEach((result) => {
      const li = document.createElement('li');
      li.textContent = result;
      resultList.appendChild(li);
    });
  }
>>>>>>> e198fb224c9586ff6072f81f2a46a2373ad917c3
