const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
	event.preventDefault(); // Prevents the form from submitting

	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;

	if (username === '' || password === '') {
		alert('Please enter a username and password');
	} else {
        if (username === "admin" && password === "password") {
        // redirect to the dashboard page
        alert(`Welcome ${username}!`);
		window.location.href = 'C:\\Users\\utkar\\OneDrive\\vscode\\html\\login gui page\\dashboard.html';
      } 
      else if(username === "root" && password === "1900") {
        // redirect to the dashboard page
        alert(`Welcome ${username}!`);
		window.location.href = 'C:\\Users\\utkar\\OneDrive\\vscode\\html\\login gui page\\dashboard.html';
      } 
      else {
        alert("incorrect username or password");
        document.getElementById('username').value="";
        document.getElementById('password').value="";
      }
		// Code to check if the username and password are valid and redirect to the dashboard page
		// You can replace this code with your own authentication system
		
	}
});
