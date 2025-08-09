import "./app.min.js";
function preloader() {
  const preloaderImages = document.querySelectorAll("img");
  const htmlDocument = document.documentElement;
  const isPreloaded = localStorage.getItem(location.href) && document.querySelector('[data-fls-preloader="true"]');
  if (preloaderImages.length && !isPreloaded) {
    let setValueProgress = function(progress2) {
      showPecentLoad ? showPecentLoad.innerText = `${progress2}%` : null;
      showLineLoad ? showLineLoad.style.width = `${progress2}%` : null;
    }, imageLoaded = function() {
      imagesLoadedCount++;
      progress = Math.round(100 / preloaderImages.length * imagesLoadedCount);
      const intervalId = setInterval(() => {
        counter >= progress ? clearInterval(intervalId) : setValueProgress(++counter);
        counter >= 100 ? addLoadedClass() : null;
      }, 10);
    };
    const preloaderTemplate = `
			<div class="fls-preloader">
				<div class="fls-preloader__body">
					<div class="fls-preloader__counter">0%</div>
				</div>
			</div>`;
    document.body.insertAdjacentHTML("beforeend", preloaderTemplate);
    document.querySelector(".fls-preloader");
    const showPecentLoad = document.querySelector(".fls-preloader__counter"), showLineLoad = document.querySelector(".fls-preloader__line span");
    let imagesLoadedCount = 0;
    let counter = 0;
    let progress = 0;
    htmlDocument.setAttribute("data-fls-preloader-loading", "");
    htmlDocument.setAttribute("data-fls-scrolllock", "");
    preloaderImages.forEach((preloaderImage) => {
      const imgClone = document.createElement("img");
      if (imgClone) {
        imgClone.onload = imageLoaded;
        imgClone.onerror = imageLoaded;
        preloaderImage.dataset.src ? imgClone.src = preloaderImage.dataset.src : imgClone.src = preloaderImage.src;
      }
    });
    setValueProgress(progress);
    const preloaderOnce = () => localStorage.setItem(location.href, "preloaded");
    document.querySelector('[data-fls-preloader="true"]') ? preloaderOnce() : null;
  } else {
    addLoadedClass();
  }
  function addLoadedClass() {
    htmlDocument.setAttribute("data-fls-preloader-loaded", "");
    htmlDocument.removeAttribute("data-fls-preloader-loading");
    htmlDocument.removeAttribute("data-fls-scrolllock");
  }
}
document.addEventListener("DOMContentLoaded", preloader);
document.addEventListener("visibilitychange", () => {
  const animatedElements = document.querySelectorAll(".gradient-bg div");
  animatedElements.forEach((el) => {
    el.style.animationPlayState = document.hidden ? "paused" : "running";
  });
});
document.addEventListener("DOMContentLoaded", () => {
  const tempToggle = document.querySelector(".temp-toggle");
  const celsiusElem = document.querySelector(".left-items__temp-value.celsius");
  const fahrenheitElem = document.querySelector(
    ".left-items__temp-value.fahrenheit"
  );
  document.querySelector(".right-items__feels-like.celsuis");
  document.querySelector(
    ".right-items__feels-like.fahrenheit"
  );
  if (tempToggle) {
    tempToggle.addEventListener("click", (event) => {
      if (event.target.classList.contains("temp-toggle__button")) {
        tempToggle.querySelectorAll(".temp-toggle__button").forEach((button) => {
          button.classList.remove("toggle__button-active");
        });
        event.target.classList.add("toggle__button-active");
        const selectedUnit = event.target.dataset.unit;
        if (selectedUnit === "celsius") {
          celsiusElem.classList.add("temp-visible");
          celsiusElem.classList.remove("temp-hidden");
          fahrenheitElem.classList.remove("temp-visible");
          fahrenheitElem.classList.add("temp-hidden");
        } else if (selectedUnit === "fahrenheit") {
          fahrenheitElem.classList.add("temp-visible");
          fahrenheitElem.classList.remove("temp-hidden");
          celsiusElem.classList.remove("temp-visible");
          celsiusElem.classList.add("temp-hidden");
        }
      }
    });
  }
});
