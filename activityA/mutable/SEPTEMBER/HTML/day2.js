document.getElementById("signup-form").addEventListener("submit", function(event) {
  event.preventDefault();  // Prevent form submission for validation
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;

  if (password !== confirmPassword) {
      alert("Passwords do not match!");
  } else {
      alert("Successfully signed up!");
      // You can process the form data here or send it to the server
  }
});

document.querySelector(".close-btn").addEventListener("click", function() {
  document.querySelector(".container").style.display = "none";
});
