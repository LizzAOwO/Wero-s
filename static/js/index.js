const dads = document.querySelector('h1')
        const mydata = JSON.parse(JSON.parse(document.getElementById('mydata').textContent))    //por algun motivo necesita doble JSON.parse, el primero parece
        console.log(mydata)                                                                     //que limpia la entrada y el segundo lo convierte en json (?)
        