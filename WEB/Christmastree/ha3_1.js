document.getElementById('lichter').addEventListener('click', () => {
    const farbe = document.getElementById('farbe').value;
    const snowContainer = document.getElementById('snowContainer');
    const display = document.getElementById('tannenbaum');

    // Очистити ялинку перед додаванням нових лампочок
    display.innerHTML = '';

    let lichtColor;

    // Встановити колір лампочок залежно від вибраного кольору
    if (farbe === 'rot') {
        lichtColor = '#fa0227';
    } else if (farbe === 'blau') {
        lichtColor = '#0760e3';
    } else if (farbe === 'gelb') {
        lichtColor = '#f1e212';
    }

    // Список координат для лампочок у межах трикутника
    const positions = [
        { left: -18, top: 50 }, // Ліва середина
        { left: -5, top: 55 }, // Права середина
        { left: 10, top: 60 }, // Лівий низ
        { left: 25, top: 65 }, // Лівий низ

        { left: -49, top: 115 }, // Ліва середина
        { left: -34, top: 120 }, // Ліва середина
        { left: -19, top: 125 }, // Права середина
        { left: -4, top:130 }, // Лівий низ
        { left: 11, top: 135 }, // Центр низу
        { left: 26, top: 140 }, // Правий низ
        { left: 41, top: 145 }, // Основа
        { left: 56, top: 150 }, // Ліва середина
        { left: 71, top: 155 }, // Ліва середина

        { left: -88, top: 190 }, // Ліва середина
        { left: -73, top: 195 }, // Ліва середина
        { left: -58, top: 200 }, // Ліва середина
        { left: -43, top: 205 }, // Ліва середина
        { left: -28, top: 210 }, // Ліва середина
        { left: -13, top: 215}, // Права середина
        { left: 2, top: 220}, // Лівий низ
        { left: 17, top: 225 }, // Центр низу
        { left: 32, top: 230 }, // Правий низ
        { left: 47, top: 235 }, // Основа
        { left: 62, top: 240 }, // Ліва середина
        { left: 77, top: 245 }, // Ліва середина
        { left: 92, top: 250 }, // Основа
        { left: 107, top: 255 }, // Ліва середина
        { left: 122, top: 260 }, // Ліва середина
    ];

    // Додати лампочки на зазначені координати
    positions.forEach(position => {
        const lampe = document.createElement('div');
        lampe.classList.add('lichter');
        lampe.style.left = position.left + 'px';
        lampe.style.top = position.top + 'px';
        lampe.style.backgroundColor = lichtColor; // Колір лампочки
        display.appendChild(lampe);
    });

    function createSnowflake() {
        const snowflake = document.createElement('div');
        snowflake.classList.add('snowflake');

        // Випадкова горизонтальна позиція
        snowflake.style.left = Math.random() * 100 + '%';

        // Випадкові тривалість анімації та розмір
        snowflake.style.animationDuration = Math.random() * 3 + 2 + 's';
        snowflake.style.animationDelay = Math.random() * 5 + 's';
        snowflake.style.width = snowflake.style.height = Math.random() * 5 + 5 + 'px';

        snowContainer.appendChild(snowflake);
    }

    for (let i = 0; i < 50; i++) {
        const snowflake = document.createElement('div'); // створюємо елемент
        snowflake.classList.add('snowflake'); // додаємо клас

        // Випадкові позиції, затримка та швидкість
        snowflake.style.left = Math.random() * 100 + '%';
        snowflake.style.animationDuration = Math.random() * 3 + 2 + 's';
        snowflake.style.animationDelay = Math.random() * 5 + 's';

        snowContainer.appendChild(snowflake); // додаємо сніжинку до контейнера
    }
});
