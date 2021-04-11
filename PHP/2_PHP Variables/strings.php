<?php
/*
-> Strings are printed with echo
-> escape sequences with backslash like in C
-> string concatenation with operator . 

Variables
-> Declaring vs Assignment
-> Declaration with $<variable_name> = <value>
-> variable Parsing: whereever a $ is used(except comments) PHP uses a variable at some place. even in quotation marks text; you can extend the text with curly brackets
-> Variable Reassignment
-> similarly to other operators in C f.e. the concatenation operator can also be used this way: .=
-> PHP has pointers? =& is an operator for that
*/
  echo "Hello, World!";
  echo "1. Teach PHP\n";
  echo "2. Do PHP\n";
  echo "3. Learn to have \"fun\"\n";
  echo "Code"."cademy\n";
  echo "My name is:". " " . "Aleks";
  echo "\n"."tur"."duck"."en";
  $random = "I fell in love with coding :)";
  $biography="\nI fell in love with coding :)";
  $bio = "I like stuff\n".$random;
  $favorite_food = "\n"."tur"."duck"."en";
  echo $bio;
  $name ="Aleks";
  $language = "english";
  echo "<dolphin sound> ". $name . " :)"; 
  echo "\nobviously, ". $language ." isn't his first language as seen above";
  
  $noun = "house";
  $adjective = "quiet";
  $verb = "jump";
  echo "The world's most beloved $noun was very $adjective and loved to $verb every single day.";
  $noun = "garden";
  $verb = $noun;
  echo "\nI have always been obsessed with ${noun}s. I'm ${adjective}ish. I'm always ${verb}ing.";

  $sentence = "\nI'm going on a picnic, and I'm taking apples";
  echo $sentence;
  $sentence .= ", but I don't have any apples";
  echo $sentence;
  $sentence .= ", cuz I ate them. I am fat lol";
  echo $sentence;
  $add_words =& $sentence;

  $add_words .= ".\n I should Workout";
  