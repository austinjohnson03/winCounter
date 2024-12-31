let wins = 0;
let draws = 0;
let losses = 0;

function updateCounter() {
    document.getElementById('wins').textContent = `Wins: ${wins}`;
    document.getElementById('losses').textContent = `Losses: ${losses}`;

    if (draws > 0) {
        document.getElementById('draws').textContent = `Draws: ${draws}`;
    }
}

function addWin() {
    wins++;
    updateCounter();
}

function addLoss() {
    losses++;
    updateCounter();
}

function addDraw() {
    draws++;
    updateCounter();
}

function resetCounter() {
    wins = 0;
    losses = 0;
    draws = 0;
    document.getElementById('draws').textContent = ''; // Hides draws if there are none
    updateCounter();
}

function toggleBackground() {
    document.body.classList.toggle('bg-enabled');
}

updateCounter();

