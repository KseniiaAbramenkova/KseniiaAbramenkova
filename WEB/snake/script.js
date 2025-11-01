"use strict"; // Strikter Modus: vermeidet schlampige Fehler wie ungewollte globale Variablen

// === DOM-Elemente abrufen ===
const gameBoard = document.getElementById("game"); // Container für das Spielfeld
const scoreDisplay = document.getElementById("score"); // Element zur Anzeige des Punktestands
const gameOverDisplay = document.getElementById("game-over"); // Text oder Overlay für Spielende
const startBtn = document.getElementById("startBtn"); // Start-Button, um das Spiel zu starten
const highscoreBody = document.querySelector("#highscoreTable tbody"); // Tabelle für Highscore-Einträge

// === Spielfeld-Konfiguration ===
const width = 20; // Anzahl Spalten des Spielfelds
const height = 20; // Anzahl Reihen
const totalCells = width * height; // Gesamtzahl der Zellen im Spielfeld (20 x 20 = 400)
let cells = []; // Array für alle DOM-Zellen

// === Spielzustände ===
let snake = []; // Array mit Zell-Indizes, die zur Snake gehören (snake[0] = Kopf)
let direction = 1; // Bewegungsrichtung: +1 = rechts, -1 = links, -width = oben, +width = unten
let food = 0; // Index der Zelle, in der sich das Futter befindet
let interval; // Referenz auf das Intervall (für setInterval), damit man es stoppen kann
let score = 0; // Aktueller Punktestand
let username = ""; // Spielername

// === Spielfeld generieren ===
function createBoard() {
    gameBoard.innerHTML = '';  // ToDo Alles im Spielfeld-Container löschen
    cells = []; // ToDo Array leeren

    // ToDo 400 Zellen erzeugen und dem DOM hinzufügen
    for(let i=0; i<totalCells; i++){
        const cell = document.createElement('div');  // ToDo Neue Zelle erstellen
        cell.classList.add('cell');  // ToDo Klasse "cell" für CSS-Styling
        gameBoard.appendChild(cell);  // ToDo Zelle ins Spielfeld einfügen
        cells.push(cell);  // ToDo Zelle im Array speichern
    }
}

// === Snake zeichnen ===
function drawSnake() {
    snake.forEach(index => cells[index].classList.add('snake'));// ToDo Jede Snake-Zelle bekommt eine Klasse
}

// === Snake entfernen ===
function removeSnake() {
    snake.forEach(index => cells[index].classList.remove('snake'));// ToDo Klasse wieder entfernen
}

// === Futter anzeigen ===
function drawFood() {
    cells[food].classList.add('food');// ToDo Zelle als Futter markieren
}

// === Futter entfernen ===
function removeFood() {
    // ToDo Futter-Markierung entfernen
}

// === Neues Futter an zufälliger Stelle platzieren ===
function randomFood() {
    do {
        //0-399
        food = Math.floor(Math.random() * totalCells);
        // ToDo Zufällige Zelle auswählen
    } while(snake.includes(food))
        // ToDo Wiederholen, falls die Zelle zur Snake gehört
    // ToDo Position speichern
    drawFood();// ToDo Funktion Futter anzeigen
}

// === Snake bewegen ===
function move() {
    const head = snake[0]; // Aktueller Kopf
    let newHead = head + direction; // Neue Kopfposition berechnen

    // === Wandkollision prüfen ===
    if (
        (direction === 1 && head % width === width - 1) || // Rechtswand
        (direction === -1 && head % width === 0) || // Linkswand
        (direction === -width && head < width) || // Oben
        (direction === width && head >= totalCells - width) // Unten
    ) {
        return gameOver(); // Wenn Kollision: Spiel beenden
    }

    // === Kollision mit sich selbst ===
    if (snake.includes(newHead)) return gameOver();

    // === Bewegung durchführen ===
    removeSnake(); // ToDo Funktion Alte Snake entfernen
    snake.unshift(newHead);// ToDo Neuen Kopf vorne einfügen

    // === Futter gefunden? ===
    if(newHead == food) { // ToDo Wenn Futter gefunden
        removeFood(); // ToDo Futter verschwinden lassen
        score ++;// ToDo Punktestand erhöhen
        scoreDisplay.innerText = `Punkte : ${score}`;// ToDo Anzeige aktualisieren
        randomFood();// ToDo Neues Futter setzen
    } else {
        // ToDo Ansonsten
        snake.pop();// ToDo Letztes Segment entfernen (wenn kein Futter gegessen wurde)

    }

    drawSnake();// ToDo Funktion Neue Snake-Zellen anzeigen
}

// === Tastatureingabe verarbeiten ===
function control(e) {
    switch (e.key) {
        case "ArrowRight":
            if (direction !== -1) direction = 1; // Kein Rückwärtsfahren!
            break;
        case "ArrowLeft":
            if (direction !== 1) direction = -1;
            break;
        case "ArrowUp":
            if (direction !== width) direction = -width;
            break;
        case "ArrowDown":
            if (direction !== -width) direction = width;
            break;
    }
}

// === Spiel starten ===
function startGame() {
    username = prompt('Wie heiß du?'); // ToDo Namen abfragen
    if(username.trim() == "") return;// ToDo Falls leer: kein Spielstart

    // === Spielzustand zurücksetzen ===
    // ToDo Vorheriges Spiel stoppen
    // ToDo Steuerung entfernen
    // ToDo Game Over ausblenden
    // ToDo Punkte zurücksetzen
    snake = [25,24,23];// ToDo Startposition (3er-Snake in Zeile 2, Mitte)
    // ToDo Richtung = rechts

    // ToDo Punktestand anzeigen
    createBoard(); // ToDo Funktion Neues Spielfeld erzeugen
    drawSnake();// ToDo Funktion Snake anzeigen
    randomFood();// ToDo Funktion Futter setzen
    interval = setInterval(move, 200);// ToDo Bewegung alle 200ms
    document.addEventListener('keydown', control) // ToDo Steuerung aktivieren
}

// === Spiel beenden und Highscore anzeigen ===
function gameOver() {
    // ToDo Bewegung stoppen
    // ToDo Steuerung deaktivieren
    // ToDo Game Over sichtbar machen

    // === Eintrag in Highscore-Tabelle ===
    // ToDo Neue Tabellenzeile erstellen
    // ToDo Name-Zelle erstellen
    // ToDo Punkte-Zelle erstellen
    // ToDo Spielername eintragen
    // ToDo Punkte eintragen
    // ToDo Zellen zur Zeile hinzufügen
    // ToDo Punkte-Zelle erweitern
    // ToDo Zeile zur Tabelle hinzufügen
}

// === EventListener für Start-Button ===
// ToDo Klick auf Button startet das Spiel
startBtn.addEventListener('click', startGame);