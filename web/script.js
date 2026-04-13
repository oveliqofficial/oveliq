// 1. Функція відкриття вікна
function openDownloadModal() {
    const modal = document.getElementById("downloadModal");
    modal.style.display = "block";
    // Додамо анімацію появи
    modal.style.opacity = "0";
    setTimeout(() => { modal.style.opacity = "1"; modal.style.transition = "0.3s"; }, 10);
}

// 2. Функція закриття вікна
function closeDownloadModal() {
    const modal = document.getElementById("downloadModal");
    modal.style.display = "none";
}

// 3. Закривати вікно, якщо натиснути на темний фон поза ним
window.onclick = function(event) {
    const modal = document.getElementById("downloadModal");
    if (event.target == modal) {
        closeDownloadModal();
    }
}

// 4. console logo
window.onload = () => {
    console.log("%c OVELIQ ENGINEERING ", "background: #000; color: #fff; font-size: 20px; font-weight: bold; border: 1px solid #222; padding: 10px;");
    console.log("Kernel: Operational (Alpha 1.0)");
};
