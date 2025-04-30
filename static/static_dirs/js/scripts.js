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

  // active link
  const links = document.querySelectorAll(".type-link");
  const currentPath = window.location.pathname;
  links.forEach(link => {
      if (link.pathname === currentPath) {
          link.classList.add("active");
      }
  });
});
