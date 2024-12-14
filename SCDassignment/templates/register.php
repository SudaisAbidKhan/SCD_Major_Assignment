<?php
   include 'config.php';

   if ($_SERVER["REQUEST_METHOD"] == "POST") {
       $name = $_POST['name'];
       $email = $_POST['email'];
       $password = password_hash($_POST['password'], PASSWORD_BCRYPT);

       $sql = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)";
       $stmt = $conn->prepare($sql);
       $stmt->bind_param("sss", $name, $email, $password);

       if ($stmt->execute()) {
           echo "Registration successful. You can now <a href='login.html'>login</a>.";
       } else {
           echo "Error: " . $stmt->error;
       }
   }
   ?>
