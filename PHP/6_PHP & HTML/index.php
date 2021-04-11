<?php
/*
PHP -> Backend language for web space and HTML, to create dynamic HTML instead of static

Front-End: Client side development -> consists of all the elements of a website sent to a client upon request
Back-End: how the site operates. Server sends html and css sites, so front end gets displayed on the browser
Consists at least of:
-> Web Server: listens for requests from clients and sends back responses
-> Application Server: Collection of programming logic which is needed to deliver dynamic content to a client. The application server will often handle other tasks such as site security & interacting with data
-> Database: stores important information;

Interessting: in the example code, all of the data is defined at the top and then the HTML stuff gets done. And they also use multiple opening and closing tags. 

HTML Form handling
Short for for PHP tags: <?php echo <p> random paragraph </p>";?> -> <?="<p> random paragraph </p>";?>
Superglobals
GET -> form entries are passed as parameters in a URL query; 

<?= is shorthand for <?php echo.
PHP provides superglobals which can be accessed anywhere in the script.
    $_GET is an associative array containing data from a GET request.
    $_POST is an associative array containing data from a POST request.
    $_REQUEST is an associative array containing data from both GET and POST requests. It should only be used if you don’t care which method was used.
The array keys in the PHP request superglobals are set by the name attributes in the HTML form, which need to be unique.
The action attribute is used to specify which file should handle data from the form request.


*/

?>
<?php 
$about_me = [
  "name" => "Aisle Nevertell",
  "birth_year" => 1902,
  "favorite_food" => "pizza"
];

function calculateAge ($person_arr){
  $current_year = date("Y");
  $age = $current_year - $person_arr["birth_year"];
  return $age;
}
?>
<h1>Welcome!</h1>
<h2>About me:</h2>
<?php
#Add your code here
  
?>

<h2>Now tell me a little about you.</h2>
<?//************************ */?>
<html>

<body>
    $_REQUEST:
    <?php print_r($_REQUEST); ?>
    <br>
    $_GET:
    <?php print_r($_GET); ?>
    <br>
    $_POST:
    <?php print_r($_POST);
    ?>
    <form method="get">
        GET Form: <input type="text" name="get_name">
        <input type="submit" value="Submit GET">
    </form>
    <form method="post">
        POST Form: <input type="text" name="post_name">
        <input type="submit" value="Submit POST">
    </form>
    <a href="index.php">Reset</a>
</body>

</html>
<?//************************ */?>
<html>
<body>
<form method="GET">
Country:
<input type="text" name="country">
<br>
Language:
<input type="text" name="language">
<br>
<input type="submit" value="Submit">
</form>
<br>
<p>Your language is: <?=$_GET['language']?></p>
<p>Your country is: <?=$_GET['country']?></p>
<a href="index.php">Reset</a>
</body>
</html>