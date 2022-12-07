
const comidas = JSON.parse(JSON.parse(document.getElementById('comidas').textContent)) 
const favoritos_div = document.querySelector(".productos-favoritos")
const comida_div = document.querySelector(".productos-comida")
const bebidas_div = document.querySelector(".productos-bebidas")
const extras_div = document.querySelector(".productos-extras")
const template = document.getElementById('template').content //por algun motivo necesita doble JSON.parse, el primero parece
const fragment_favoritos = document.createDocumentFragment()
const fragment_comida = document.createDocumentFragment()                  //que limpia la entrada y el segundo lo convierte en json (?)
const fragment_bebida = document.createDocumentFragment()
const fragment_extras = document.createDocumentFragment()
const container_menu = document.querySelector(".container-menu") 
console.log(comidas)

document.addEventListener('DOMContentLoaded', () => {
    pintarComidas()
})

const fav = ["Taco de pastor", "Taco de Bistec", "Taco de suadero", "Quesadilla de tripa",
            "Horchata", "Agua de Jamaica", "Salsa Roja", "Salsa Guacamole"]

const pintarComidas = () => {
    comidas.forEach( comida => {
        var xhr = new XMLHttpRequest();
            xhr.open('HEAD', `./static/img/${comida.fields.alim_nombre}.jpg`, false);
            xhr.send();
            if (xhr.status == "404") {
                template.querySelectorAll('img')[0].src = `./static/img/logo-tacos.png`
            } else {
                template.querySelectorAll('img')[0].src = `./static/img/${comida.fields.alim_nombre}.jpg`
            }

        template.querySelectorAll('label')[0].textContent = comida.fields.alim_nombre
        template.querySelectorAll('label')[1].textContent = "$"+comida.fields.alim_precio
        template.querySelectorAll('button')[0].value = comida.pk
        
        if(comida.fields.alim_categoria == "Extra"){
            template.querySelectorAll('input')[1].max = 10
        }  
        const clone = template.cloneNode(true)
        fav.forEach( favorito => {  
            if(favorito == comida.fields.alim_nombre){
                const clone = template.cloneNode(true)
                fragment_favoritos.appendChild(clone)
                
            }
        })
        if(comida.fields.alim_categoria == "Comida"){
            fragment_comida.appendChild(clone)
        }     
        if(comida.fields.alim_categoria == "Bebida"){
            fragment_bebida.appendChild(clone)
        }  
        if(comida.fields.alim_categoria == "Extra"){
            fragment_extras.appendChild(clone)
        }  
    })
    favoritos_div.appendChild(fragment_favoritos)
    bebidas_div.appendChild(fragment_bebida)
    comida_div.appendChild(fragment_comida)
    extras_div.appendChild(fragment_extras)
}
