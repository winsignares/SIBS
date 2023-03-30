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