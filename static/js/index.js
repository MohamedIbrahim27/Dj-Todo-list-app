document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".btn-primary");
    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            var modalId = button.getAttribute("data-target");
            var modal = document.querySelector(modalId);
            var closeButton = modal.querySelector(".close");
            modal.style.display = "block";
            closeButton.addEventListener("click", function () {
                modal.style.display = "none";
            });
            window.addEventListener("click", function (event) {
                if (event.target === modal) {
                    modal.style.display = "none";
                }
            });
        });
    });
});