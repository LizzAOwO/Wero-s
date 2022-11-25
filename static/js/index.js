
const comidas = JSON.parse(JSON.parse(document.getElementById('comidas').textContent)) 
const favoritos_div = document.getElementById('favoritos-div')
const template_comida = document.getElementById('template').content //por algun motivo necesita doble JSON.parse, el primero parece
const fragment = document.createDocumentFragment()                  //que limpia la entrada y el segundo lo convierte en json (?)

console.log(comidas)
document.addEventListener('DOMContentLoaded', () => {
    pintarComidas()
})

const pintarComidas = () => {
    comidas.forEach( comida => {
        template_comida.querySelectorAll('label')[0].textContent = comida.fields.alim_nombre
        template_comida.querySelectorAll('label')[1].textContent = "$"+comida.fields.alim_precio
        template_comida.querySelectorAll('button')[0].id = comida.pk
        const clone = template_comida.cloneNode(true)
        fragment.appendChild(clone)
    })
    favoritos_div.appendChild(fragment)
}

