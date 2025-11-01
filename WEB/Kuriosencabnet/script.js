"use strict";

// 🧳 Kuriose Gegenstände: [Name, Kategorie, Beschreibung]
const objekte = [
    ["Schreiender Spiegel", "Verflucht", "Reflektiert deine größten Ängste."],
    ["Mechanisches Huhn", "Mechanisch", "Gackert in Morsezeichen."],
    ["Nebelglaskugel", "Magisch", "Zeigt nur Dinge, die du lieber nicht weißt."]
];

const liste = document.getElementById("kabinett"); //im "getElementById" der Buchstabe "d" sollte klein geschrieben werden
// 2 neue DOM-Elemente um nach Kategorie zu filtern
const details = document.getElementById("details");
const filter = document.getElementById("filter");

//alte Code
/*
objekte.forEach((eintrag, i) => {   //im "forEach" "E" muss großgeschrieben werden
    const li = document.createElement("li");
    li.innerText = eintrag[0]; // Name
    li.dataset.index = i;
    liste.appendChild(li);
});

liste.addEventListener("click", function(event) { //die Variable heißt "liste", nicht "list"
    const ziel = event.target;
    if (ziel.tagName === "li") {
        const index = ziel.dataset.index;
        const objekt = objekte[index]; // Eintrag: [Name, Kategorie, Beschreibung]
        const details = document.querySelector("#details");

        if (ziel.tagName == "li") {
            details.innerHTML = `
        <h2>${objekt[0]}</h2>
        <p><strong>Kategorie:</strong> ${objekt[1]}</p>
        <p>${objekt[2]}</p>
      `;
        }
    }
});
 */

//neue Code mit Filtern nach Kategorie und Details anzeigen

// Event-Listener für den Zufallsfundstück-Button
const zufallButton = document.getElementById("zufall");
zufallButton.addEventListener("click", function() {
    const zufallsIndex = Math.floor(Math.random() * objekte.length);
    zeigeDetails(zufallsIndex);
});

// filtern
function zeigeListe(kategorie = "Alle") {
    liste.innerHTML = ""; //Vorherige Liste leeren
    objekte.forEach((objekt, i) => {
        if (kategorie === "Alle" || objekt[1] === kategorie) {
            const li = document.createElement("li");
            li.innerText = objekt[0];
            li.dataset.index = i;
            liste.appendChild(li);
        }
    });
}

// 📄 Функція для показу деталей
function zeigeDetails(index) {
    const objekt = objekte[index];
    details.innerHTML = `
        <h2>${objekt[0]}</h2>
        <p><strong>Kategorie:</strong> ${objekt[1]}</p>
        <p>${objekt[2]}</p>
    `;
}

// Liste beim Start anzeigen
zeigeListe();

// Klick-Event auf die Liste
liste.addEventListener("click", function(event) {
    const ziel = event.target;
    // Nur wenn ein <li>-Element angeklickt wurde
    if (ziel.tagName === "LI") {
        zeigeDetails(ziel.dataset.index); // Details anzeigen
    }
});

// Event-Listener für die Filterauswah
filter.addEventListener("change", function() {
    zeigeListe(this.value);  // Liste nach gewählter Kategorie anzeigen
    details.innerHTML = "";  // Details löschen
});
