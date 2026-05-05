document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "admin" && password === "123456") {
        window.location.href = "dashboard.html";
    } else {
        const message = document.getElementById("message");
        message.style.color = "red";
        message.textContent = "Invalid credentials!";
    }
});