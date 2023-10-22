const express = require("express");
const mysql = require("mysql");

const app = express();

// Create a MySQL connection pool
const pool = mysql.createPool({
  connectionLimit: 10,
  host: "localhost",
  user: "root",
  password: "1900",
  database: "log",
});

// Handle POST requests to the /register endpoint
app.post("/register", (req, res) => {
  // Get the registration data from the request body
  const registrationData = req.body;

  // Insert a new record into the users table
  pool.query(
    "INSERT INTO users (name, email, dob) VALUES (?, ?, ?)",
    [registrationData.name, registrationData.email, registrationData.dob],
    (error, results) => {
      if (error) {
        console.error(error);
        res.sendStatus(500);
      } else {
        res.sendStatus(200);
      }
    }
  );
});

// Start the server
app.listen(3000, () => {
  console.log("Server listening on port 3000");
});
