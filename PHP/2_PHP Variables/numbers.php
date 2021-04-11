<?php
/*
Numbers
-> integer, float
-> addition & Subtraction (small hint: if you use flaot numbers and they round up to a full number like 9.9 +.1 it will print 10 instead of 10.0)
-> division & multiplication (same thing here: division also returns an integer if its a full number, otherwise a float)
-> Exponentiation with ** operator
-> Modulo with % operator returns the remainder after a division, which would result in a fraction
-> operation order like in math: PEMDAS: parentheses, exponents, multiplication, division, addition, subtraction
-> short forms like in C

*/
$dollars = 100;
$cents = 0.99;
echo $dollars;
echo "\n$cents";
echo 11+1;
$num_languages = 4;
$months = 11;
$days= 16*$months;
$days_per_language=$days / $num_languages;
echo $days_per_language;
echo 8**2;
echo 82%6;

$start=94;
$coffee = 4.25;
$friend = 7;
$meal = 23.5 *1.2;
$moneyground = 20/4;
echo $start - $coffee + $friend - $meal + $moneyground; 

?>