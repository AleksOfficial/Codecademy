<?php
/*
  PHP can store in arrays data of different datatype
  implode function -> prints array and uses the seperator provided in the function
  print_r function -> prints number array in a readable manner
  in PHP you can add a dataentry to an array by writing the variable name and adding brackets to the end
  array_push() -> Adds an array to another one to the end
  array_pop() -> returns the last element of an array and removes it from there
  array_shift() -> returns first element of an array and removes it from there
  array_unshift() -> Adds array to the front of an existing array
*/

$first_array = array("0",1,"2",3,"4");
echo count($first_array);
//short syntax*******************************
$short_syn = ["0",1,"2",3,"4"];

//*******************************************
$message = ["Oh hey", " You're doing great", " Keep up the good work!\n"];

$favorite_nums = [7, 201, 33, 88, 91];
echo implode("!", $message);
print_r($favorite_nums);

//*******************************************
$round_one = ["X", "X", "first winner"];
$round_two = ["second winner", "X", "X", "X"];
$round_three = ["X", "X", "X", "X", "third winner"];

$winners = array($round_one[2],$round_two[0],$round_three[4]);
print_r($winners);

//*******************************************
$change_me = [3, 6, 9];
$change_me[]="oof";
$change_me[]=1;
$change_me[1]="tadpole";
print_r($change_me);
//*******************************************

$stack = ["wild success", "failure", "struggle"];
array_push($stack,"blocker","impediment");
while(count($stack)>1)
{
  array_pop($stack);
}
print_r($stack);
//*******************************************
$record_holders = [];
array_unshift($record_holders,"Tim Montgomery","Maurice Greene", "Donovan Bailey","Leroy Burrell","Carl Lewis");

array_shift($record_holders);
array_unshift($record_holders,"Justin Gatlin", "Asafa Powell");
array_shift($record_holders);
array_unshift($record_holders,"Usain Bolt");
print_r($record_holders);
//*******************************************
$treasure_hunt = ["garbage", "cat", 99, ["soda can", 8, ":)", "sludge", ["stuff", "lint", ["GOLD!"], "cave", "bat", "scorpion"], "rock"], "glitter", "moonlight", 2.11];

print($treasure_hunt[3][4][2][0]);
?>
