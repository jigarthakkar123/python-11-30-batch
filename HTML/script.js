function signUpValidation() {
    var username = document.getElementById("signup-username").value;
    var password = document.getElementById("signup-password").value;
    var confirmPassword = document.getElementById("signup-confirm-password").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match");
        return false;
    }

    // Additional validation logic can be added here

    alert("Sign up successful");
    return true;
}

function loginValidation() {
    var username = document.getElementById("login-username").value;
    var password = document.getElementById("login-password").value;

    // Validation logic can be added here, such as checking against a database

    alert("Login successful");
    return true;
}
