login = () => {
    let usuario = document.querySelector('input[type=text]').textContent
    let senha = document.querySelector('input[type=password]').textContent

    fetch(`http://localhost:3000/login/${usuario}`)
        .then(response => response.json())
        .then(data => {
            
        })
        .catch(error => {
            console.error('Error:', error);
        });
}