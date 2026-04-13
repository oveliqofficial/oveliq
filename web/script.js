document.addEventListener('DOMContentLoaded', () => {
    // 1. Smooth Scroll for Hero Button
    document.getElementById('exploreBtn').addEventListener('click', () => {
        document.getElementById('specs').scrollIntoView({ behavior: 'smooth' });
    });

    // 2. Cursor Glow Follow
    const glow = document.getElementById('glow');
    document.addEventListener('mousemove', (e) => {
        glow.style.left = e.clientX + 'px';
        glow.style.top = e.clientY + 'px';
    });

    // 3. FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        item.querySelector('.faq-question').addEventListener('click', () => {
            faqItems.forEach(i => { if (i !== item) i.classList.remove('active'); });
            item.classList.toggle('active');
        });
    });

    // 4. Console Watermark
    console.log("%c Oveliq Systems %c Active ", "color: #fff; background: #0078d4; padding: 5px; font-weight: bold;", "color: #fff; background: #333; padding: 5px;");
});
