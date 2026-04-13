document.addEventListener('DOMContentLoaded', () => {
    // 1. Анімація появи карток при скролі (Intersection Observer)
    const cards = document.querySelectorAll('.card');
    const observerOptions = {
        threshold: 0.1 // Спрацює, коли 10% карти видно
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease-out';
        observer.observe(card);
    });

    // 2. Ватермарк у консолі (залишаємо твою фішку)
    console.log(
        "%c Oveliq OS ", 
        "color: white; background: black; padding: 5px 10px; border-radius: 3px; font-weight: bold; font-size: 1.2em;"
    );
    console.log("Status: Operational");
});
