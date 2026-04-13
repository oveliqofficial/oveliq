const input = document.getElementById('terminal-input');
const content = document.getElementById('terminal-content');

// Функція для додавання нового рядка в термінал
function addLog(text, type = 'bot-msg') {
    const p = document.createElement('p');
    p.textContent = text;
    p.className = type;
    content.appendChild(p);
    // Автоматична прокрутка вниз
    content.scrollTop = content.scrollHeight;
}

// Функція обробки команд
function processCommand(cmd) {
    const cleanCmd = cmd.toLowerCase().trim();
    
    // Ехо команди користувача
    addLog(`> ${cmd}`, 'user-cmd');

    if (cleanCmd === 'help') {
        addLog('Доступні команди: about, status, contact, clear');
    } else if (cleanCmd === 'about') {
        addLog('Oveliq Systems — проект з розробки захищеної екосистеми.');
    } else if (cleanCmd === 'status') {
        addLog('Oveliq Network: ONLINE | Core v2.1.0: Active');
    } else if (cleanCmd === 'contact') {
        addLog('Приєднуйтесь до нашого Discord: discord.gg/SypXW72qQu');
    } else if (cleanCmd === 'clear') {
        content.innerHTML = ''; // Очистити консоль
        addLog('Terminal cleared. Oveliq Console v2.0', 'bot-msg');
    } else if (cleanCmd === '') {
        // Нічого не робити
    } else {
        addLog(`Помилка: Команда '${cleanCmd}' не знайдена. Спробуйте 'help'.`, 'error-msg');
    }
}

// Слухач натискання клавіш
input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const command = input.value;
        processCommand(command);
        input.value = ''; // Очистити поле вводу
    }
});
