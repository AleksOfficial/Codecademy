<?php
// A basic calculator that submits stuff through a form and sends it over the superglobal variable to another php file.
//I'll just post the code snippets of that here. I don't think I'll go into further detail. 
?>

<?//File One: index.php?>
<html>

<body>
  <form method="get" action="addition.php">
    <h3>Addition!</h3>
    <input type="number" name="Zahl1">+
    <input type="number" name="Zahl2">
    <input type="submit" value="go!">
  </form>

  <form method="get" action="division.php">
    <h3>Division!</h3>
    <input type="number" name="Zahl1">:
    <input type="number" name="Zahl2">
    <input type="submit" value="go!">
  </form>
  <a href="index.php">Reset</a>
</body>

</html>

<?//File two: addition.php ?>
<html>

<body>
  <?php
  $z1 = $_GET['Zahl1'];
  $z2 = $_GET['Zahl2'];
  $erg = $z1 + $z2;
  echo "$z1 + $z2 = $erg";
  ?>
  <br>
  <a href="index.php">Reset</a>
</body>

</html>

<?//File three: division.php?>
<html>

<body>
  <?php
  $z1 = $_GET['Zahl1'];
  $z2 = $_GET['Zahl2'];
  if ($z2 != 0) {
    $erg = $z1 / $z2;
    echo "$z1 / $z2 = $erg";
  } else
    echo "<p>keine Division durch 0!</p>";

  ?>

  <a href="index.php">Reset</a>
</body>

</html>