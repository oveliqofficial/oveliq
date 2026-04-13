function openModal() {
    document.getElementById("downloadModal").style.display = "block";
}

function closeModal() {
    document.getElementById("downloadModal").style.display = "none";
}

// Закриття при кліку поза вікном
window.onclick = function(event) {
    let modal = document.getElementById("downloadModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

console.log("%c Oveliq OS Portal Active ", "color: black; background: white; font-weight: bold;");
