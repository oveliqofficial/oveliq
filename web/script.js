document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scroll for Button
    document.getElementById('exploreBtn').addEventListener('click', () => {
        document.getElementById('specs').scrollIntoView({ behavior: 'smooth' });
    });

    // Mouse Glow
    const glow = document.getElementById('glow');
    document.addEventListener('mousemove', (e) => {
        glow.style.left = e.clientX + 'px';
        glow.style.top = e.clientY + 'px';
    });

    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.querySelector('.faq-question').addEventListener('click', () => {
            faqItems.forEach(i => { if (i !== item) i.classList.remove('active'); });
            item.classList.toggle('active');
        });
    });
});
