// Wait until page is loaded
document.addEventListener("DOMContentLoaded", function () {
    let btn = document.getElementById("goBtn");
    btn.addEventListener("click", function () {
        window.location.href = "/contact";
    });
});
