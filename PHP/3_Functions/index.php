<?php
/*
return statement terminates the function immediately
camelCase
snake_case
kebab-case
PascalCase

*/
  function PraisePHP()
  {
    echo "PHP is just like C. and I love C";
  }
  function inflateEgo()
  {
    echo "your hair is nice. or smth.";
  }
  
  inflateEgo();

  function printStringReturnNumber()
  {
    echo "123";
    $my_num=4;
    return $my_num;
  }
$my_num=printStringReturnNumber();
echo $my_num;

function notFound()
{ 
  echo "ERROR: Page not found!\n";
  return 404;
  
}

function greetLearner()
{
  
  echo "Hello, Learner!\n";
  echo "I hope you're (still) enjoying PHP!\n";
  echo "Love, Codecademy\n";
  return "<3";
}


$error = notFound(); 
$heart = greetLearner();

echo "I received a $error, but it's ok because I also received $heart.";

function first()
{
  return "You did it!\n";
}

function second()
{
  return "You're amazing!\n";
}

function third()
{
  return "You're a coding hero!\n";
}
echo first().second().third();

function createVacuum(){

}
echo createVacuum() * 10; //prints 0 obv

function increaseEnthusiasm($string){
  return $string."!";
}
function repeatThreeTimes($three){
  return $three.$three.$three;
}
echo increaseEnthusiasm("lol");
echo repeatThreeTimes("hello WOrlD!");
echo increaseEnthusiasm(repeatThreeTimes("hey"));


function calculateArea($height,$width){
  return $height*$width;
}
function calculateVolume($height,$width,$depth)
{
  return calculateArea($height,$width)*$depth;
}
echo calculateArea(1,1);
echo calculateVolume(1,1,1);

function calculateTip($cost,$tip=20)
{return $cost+$cost*$tip/100;}
echo calculateTip(100,25);
echo "\n".calculateTip(100);


#scope of variable
# -> variable can be globally instantiated, and called in a function with the global attribute

/*
$language = "PHP";
$topic = "scope";

function generateLessonName($language, $concept)
{
  return $language . ": " . $concept;
}

echo generateLessonName($language, $topic);
*/

$language = "PHP";
$topic = "scope";

function generateLessonName($concept)
{
  global $language;
  return $language . ": " . $concept;
}

echo generateLessonName($topic);


?>