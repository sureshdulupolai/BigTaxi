const rating = parseFloat("{{ totalOutOf }}");
const fullStars = Math.floor(rating);
const halfStar = (rating - fullStars) >= 0.5 ? 1 : 0;
const emptyStars = 5 - fullStars - halfStar;

let starHTML = '';
for (let i = 0; i < fullStars; i++) {
    starHTML += '<i class="fas fa-star"></i>';
}
if (halfStar) {
    starHTML += '<i class="fas fa-star-half-alt"></i>';
}
for (let i = 0; i < emptyStars; i++) {
    starHTML += '<i class="far fa-star"></i>';
}

document.getElementById('star-rating').innerHTML = starHTML;


document.addEventListener("DOMContentLoaded", function () {
const toggles = document.querySelectorAll(".toggle-text");

toggles.forEach(function (toggle) {
    toggle.addEventListener("click", function (e) {
    e.preventDefault();
    const cardText = this.closest(".card-text");
    const shortText = cardText.querySelector(".short-text");
    const fullText = cardText.querySelector(".full-text");
    const brTag = cardText.querySelector(".toggle-break");

    if (fullText.classList.contains("d-none")) {
        shortText.classList.add("d-none");
        fullText.classList.remove("d-none");
        brTag.classList.remove("d-none");
        this.textContent = "Show less";
    } else {
        shortText.classList.remove("d-none");
        fullText.classList.add("d-none");
        brTag.classList.add("d-none");
        this.textContent = "Read more";
    }
    });
});
});