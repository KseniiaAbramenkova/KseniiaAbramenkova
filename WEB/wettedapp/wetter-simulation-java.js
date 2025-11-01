document.getElementById('generateWeather').addEventListener('click', () => {
const weather = document.getElementById('weather').value;
const temperature = parseInt(document.getElementById('temperature').value);
const display = document.getElementById('weatherDisplay');

document.getElementById('tempValue').textContent = temperature + "°C";
// reset display
display.innerHTML = '';

let backgroundColor;

// color based on temp

if(temperature < 0) {
    backgroundColor = '#b0e0e6';
} else if (temperature >= 0 && temperature <= 20) {
    backgroundColor = '#87ceeb'
} else {
    backgroundColor= '#ffdead'
}

document.body.style.backgroundColor = backgroundColor;

if (weather === 'sunny') {
    const sun = document.createElement('div');
    sun.id = 'sun';
    sun.style.width = temperature + 50 + 'px';
    sun.style.height = temperature + 50 + 'px';
    display.appendChild(sun);
} else if (weather === 'rainy') {
    for ( let i = 0; i < 50; i++) {
        console.info(i)
        const raindrop = document.createElement('div'); //html element
        raindrop.classList.add('raindrop'); //class for html element
        raindrop.style.left = Math.random() * 100 + '%'; // random position raindrop
        raindrop.style.animationDuration = Math.random() * 2 + 1 + 's';
        raindrop.style.animationDelay = Math.random() * 1 + 's';
        display.appendChild(raindrop);
    }
} else if (weather === 'snowy') {
    for ( let i = 0; i < 50; i++) {
        console.info(i)
        const snowflake = document.createElement('div'); //html element
        snowflake.classList.add('snowflake'); //class for html element
        snowflake.style.left = Math.random() * 100 + '%'; // random position raindrop
        snowflake.style.animationDuration = Math.random() * 2 + 1 + 's';
        snowflake.style.animationDelay = Math.random() * 1 + 's';
        display.appendChild(snowflake);
    }

}

})