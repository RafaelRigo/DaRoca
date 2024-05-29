let c = 1
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

function url() {
    let urlParams = new URLSearchParams(window.location.search)
    let valorInput = urlParams.get('input')
    document.getElementById('txt-buscar').value = valorInput;
}

function filtro() {           
    let classes = ['fruta', 'legume', 'verdura'];

    for (let alimento of classes) {
        let al = document.querySelectorAll('.' + alimento + 's');
        if (document.querySelector('#' + alimento).checked === false) {
            for (let i of al) {
                i.style.display = 'none';
            }
        } else {
            for (let j of al) {
                j.style.display = 'block';
            }
        }
    }
}

const carregarProdutos = () => {
    fetch('http://localhost:3000/produtos')
        .then(response => response.json())
        .then(data => {

            let produtos = data;
            let div = document.getElementById('mercadoria')
            let html = '';

            produtos.forEach(produto => {
                html += `
                <div class="it ${produto["categoria"]}s">
                <img class="img" src="${produto["imagem"]}">
                <div class="info">
                
                <h2>${produto["nome"]} - ${produto["descricao"]}</h2>

                <h4>${produto["categoria"].charAt().toUpperCase() + produto["categoria"].slice(1)}</h4>

                <h3>R$ ${produto["valor"].toFixed(2).toString().replace(".", ",")}</h3>

                <button class="qtd" onclick="somar('cont${produto["id"]}')">+</button>
                <p class="cont${produto["id"]}">1</p>
                <button class="qtd" onclick="sub('cont${produto["id"]}')">-</button>

                <button class="add" onclick="reset()">adicionar</button>
                </div></div>
                `
            });

            div.innerHTML = html
        })
        .catch(error => {
            console.error('Error:', error);
        });
}