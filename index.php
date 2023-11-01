<?php

echo "Hi";
$name = "mahdi";
if (isset($_POST["Hi"])) {
    $name = $_POST["name"];
    $password = $_POST["password"];
    $email = $_POST["email"];
    $password2 = $_POST["password"];
    $username = $_POST["username"];
    if(empty($name) || empty($password) || empty($email))
    {
        echo "Hi ";
        exit;
    }
}
$a = 4;
echo "this is huge";

?>
