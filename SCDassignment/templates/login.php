<?php
   session_start();
   include 'config.php';

   if ($_SERVER["REQUEST_METHOD"] == "POST") {
       $email = $_POST['email'];
       $password = $_POST['password'];

       $sql = "SELECT * FROM users WHERE email = ?";
       $stmt = $conn->prepare($sql);
       $stmt->bind_param("s", $email);
       $stmt->execute();
       $result = $stmt->get_result();

       if ($result->num_rows > 0) {
           $user = $result->fetch_assoc();
           if (password_verify($password, $user['password'])) {
               $_SESSION['user_id'] = $user['id'];
               $_SESSION['user_name'] = $user['name'];
               header("Location: index.html");
           } else {
               echo "Invalid password.";
           }
       } else {
           echo "No user found with that email.";
       }
   }
   ?>
