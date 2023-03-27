// Definimos el componente
class Component {
  constructor(id, template) {
    this.element = document.getElementById(id);
    this.template = template;
  }

  render() {
    this.element.innerHTML = this.template.innerHTML;
  }
}

// Creamos una instancia del componente
const templateContainer = new Component('template-container', document.getElementById('template1'));

// Cambiamos la plantilla en respuesta a un evento
const changeTemplateBtn = document.getElementById('change-template-btn');
changeTemplateBtn.addEventListener('click', () => {
  templateContainer.template = document.getElementById('template2');
  templateContainer.render();
});


function incorporarplantilla(id, ruta){
    const objto = document.getElementById(id);
    objto.innerHTML = ruta    
}