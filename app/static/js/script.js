function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}

var typed = new Typed(".typed_text", {
  strings: ["Cloud Engineer", "Software Developer", "DevSecOps Engineer", "Cybersecurity Enthusiast"],
  typeSpeed: 50,
  backSpeed: 80,
  loop: true
});
