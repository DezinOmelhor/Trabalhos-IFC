// Selecionar os botões pelos IDs
const playButton = document.getElementById('play-button'); // Botão "Jogar Solo"
const playButton2 = document.getElementById('play-button2'); // Botão "Jogar Versus"

// Adicionar eventos de clique para cada botão
playButton.addEventListener('click', function() {
    window.location.href = "Sologame.html";
});                                                 //Ter certeza que os nomes estão identicos

playButton2.addEventListener('click', function() {
    window.location.href = "Versusgame.html";
});