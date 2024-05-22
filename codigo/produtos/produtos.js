var c = 1
function reset(){
    c = 1
}

function somar(classe){
    c += 1
    document.querySelector('.'+classe).innerHTML = c
}

function sub(classe){
    if (c > 1){
        c -= 1
    }
    document.querySelector('.'+classe).innerHTML = c
}
window.onload = function() {
    var urlParams = new URLSearchParams(window.location.search)
    var valorInput = urlParams.get('input')
    document.getElementById('txt-buscar').value = valorInput;
    
    // carregar produtos a partir de arquivo JSON
    const div = document.getElementById('mercadoria')
    
}

function filtro() {           
    let classes = ['fruta', 'legume', 'verdura'];

    for (var alimento of classes) {
        var al = document.querySelectorAll('.' + classes[alimento] + 's');
        if (document.querySelector('#' + classes[alimento]).checked === false) {
            for (var i of al) {
                al[i].style.display = 'none';
            }
        } else {
            for (var j of al) {
                al[j].style.display = 'block';
            }
        }
    }
}

