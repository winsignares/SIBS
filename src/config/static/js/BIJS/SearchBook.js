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