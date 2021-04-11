<?php
/*
echo is not a function!
gettype -> obv what it does
var_dump -> prints details about argument
string functions
strrev -> reverses string
strtolower -> everything will be lower
str_repeat -> repeats string to the amount of the second argument
substring -> portion of a string; substr_count counts instances of substr. in str
number func.
abs function -> returns absolute value of number
round function -> duhh already used. 
rand -> random integer, in PHP
important for the docs: [] is optional if it is in the function descriptions
nice this exercise is about finding built in functions in PHP
*/

namespace Codecademy;

$first = "Welcome to the magical world of built-in functions.";
  
$second = 82137012983; 

//Write your code below:
echo gettype($first)."\n";
echo gettype($second)."\n";
var_dump($first)."\n";
var_dump($second)."\n";

echo strrev(".pu ti peeK .taerg gniod er'uoY");
echo strtolower("SOON, tHiS WILL Look NoRmAL.");
echo str_repeat("\nThere's no place like home.\n",3);

$essay_one = "I really enjoyed the book. I thought the characters were really interesting. The plot of the novel was really engaging. I really felt the characters' emotions. They were really well-written. I really wish the ending had been different though.";
  
$essay_two = "Obviously this is a really good book. You obviously would not have made us read it if it wasn't. I felt like the ending was too obvious though. It was so obvious who did it right away. I think the thing with the light was obviously a metaphor for life. It would have been better if the characters were less obvious about their secrets.";  

echo substr_count($essay_one,"really");
echo substr_count($essay_two,"obvious");

function calculateDistance($distance1,$distance2)
{
  return abs($distance1-$distance2);
}
function calculatetip($funds)
{
  return round($funds+$funds*0.18,0);
}

echo getrandmax();
echo "\n";
echo rand();
echo "\n";
echo rand(1,52);

function convertToShout($string)
{
  return strtoupper($string)."!";
}

function tipGenerously($funds)
{
  return ceil($funds+$funds*.2,0);
}
function calculateCircleArea($diameter)
{
  return($diameter**2 * pi()/4);
}

?>
