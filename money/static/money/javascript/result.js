document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".comma-input");

    inputs.forEach(input => {
        input.addEventListener("input", function () {
            let value = this.value.replace(/,/g, ""); // 既存のカンマを削除
            if (!isNaN(value) && value !== "") {
                this.value = Number(value).toLocaleString();
            }
        });

        input.addEventListener("blur", function () {
            let value = this.value.replace(/,/g, "");
            if (!isNaN(value) && value !== "") {
                this.value = Number(value).toLocaleString();
            }
        });
    });
});