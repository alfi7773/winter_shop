// let currentIndex = 0;
//         const slides = document.querySelector(".slider").children;
//         const totalSlides = slides.length;
        
//         function moveSlide(step) {
//             currentIndex = (currentIndex + step + totalSlides) % totalSlides;
//             document.querySelector(".slider").style.transform = `translateX(-${currentIndex * 100}%)`;
//         }
document.addEventListener("DOMContentLoaded", function () {
    let currentIndex = 0;
    const slides = document.querySelectorAll(".slide");
    const slider = document.querySelector(".slider");
    const totalSlides = slides.length;

    function moveSlide(step) {
        currentIndex = (currentIndex + step + totalSlides) % totalSlides;
        slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    document.querySelector(".prev").addEventListener("click", () => moveSlide(-1));
    document.querySelector(".next").addEventListener("click", () => moveSlide(1));
});



function scrollSlider(direction) {
    const slider = document.getElementById("productSlider");
    const scrollAmount = 300; // Шаг прокрутки
    slider.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
}
