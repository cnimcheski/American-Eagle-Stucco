const sr = ScrollReveal ({
    distance: '65px',
    duration: 1000,
    delay: 0,
    reset: true
});

sr.reveal('.home-image-overlay-container', {origin: 'top'})
sr.reveal('.header-image-overlay', {origin: 'top'})


const faqs = document.querySelectorAll(".faq");

faqs.forEach(faq => {
    faq.addEventListener("click", () => {
        faq.classList.toggle("active");
    });
});