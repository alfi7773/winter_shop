// let currentIndex = 0;
//         const slides = document.querySelector(".slider").children;
//         const totalSlides = slides.length;
        
//         function moveSlide(step) {
//             currentIndex = (currentIndex + step + totalSlides) % totalSlides;
//             document.querySelector(".slider").style.transform = `translateX(-${currentIndex * 100}%)`;
//         }




console.clear();

gsap.registerPlugin(ScrollTrigger);

window.addEventListener("load", () => {
  gsap
    .timeline({
      scrollTrigger: {
        trigger: ".wrapper",
        start: "top top",
        end: "+=150%",
        pin: true,
        scrub: true,
        markers: true
      }
    })
    .to("img", {
      scale: 2,
      z: 350,
      transformOrigin: "center center",
      ease: "power1.inOut"
    })
    .to(
      ".section.hero",
      {
        scale: 1.1,
        transformOrigin: "center center",
        ease: "power1.inOut"
      },
      "<"
    );
});

document.querySelectorAll('.category').forEach(item => {
  item.addEventListener('click', () => {
      let submenu = item.querySelector('.submenu');
      submenu.style.display = (submenu.style.display === 'block') ? 'none' : 'block';
  });
});



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
    const scrollAmount = 300;
    slider.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
}


document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".type-link");
    const currentPath = window.location.pathname;
  
    links.forEach(link => {
      if (link.pathname === currentPath) {
        link.classList.add("active");
      }
    });
  });
  
