<?php
/*
Associative Arrays = key -> value pairs; each key points to a value
key-value pairs printed with print_r()
unset function -> removes associated pair in array
if it has an associative key, then this one is the index. if the associative key is a high number, then the next element without a key will be the element after it
union operator + joins 2 arrays; if a key is not unique, it returns the value of the first table to be joined -> this also is true for arrays which have no associative keys
the & operator in a function for its arguments changes the value permanently. meaning it changes the origin, much like a pointer. 
*/
  $php_array = array(
    "language" => "PHP",
    "creator" => "Rasmus Lerdorf",
    "year_created" => 1995,
    "filename_extensions" => [".php",".phtml",".php3",".php4",".php5",".php7",".phps",".php-s",".pht",".phar"]);

  $php_short = ["language" => "PHP",
    "creator" => "Rasmus Lerdorf",
    "year_created" => 1995,
    "filename_extensions" => [".php",".phtml",".php3",".php4",".php5",".php7",".phps",".php-s",".pht",".phar"]];

//******************************************
  $september_hits = ["The Sixth Sense" => 22896967,"Stigmata" =>"18309666", "Blue Streak" =>19208806,"Double Jeopardy" => 23162542];

  echo implode(", ",$september_hits);
  print_r($september_hits);
//******************************************
$assignment_one = ["Alex"=> 87, "Kenny"=> 91, "Natalia"=> 91, "Lily"=> 67, "Dan"=> 81, "Kat"=> 77, "Sara" => 65];

$assignment_two = ["Alex"=> 91, "Kenny"=> 99, "Natalia"=> 100, "Lily"=> 61, "Dan"=> 88, "Kat"=> 90];

$assignment_three = ["Alex"=> 78, "Kenny"=> 92, "Natalia"=> 94, "Lily"=> 79, "Dan"=> 73, "Sara" => 61];

$student_name = "Alex";

  $assignment_two["Sara"]=65;
  $assignment_three["Kat"]=97;
$dans_grades=[$assignment_one["Dan"],$assignment_two["Dan"],$assignment_three["Dan"]];

echo $assignment_two[$student_name];

$my_car = [
  "oil" => "black and clumpy",
  "brakes" => "new",
  "tires" => "old with worn treads",
  "filth" => "bird droppings", 
  "wiper fluid" => "full", 
  "headlights" => "bright"
];
print_r($my_car);
$my_car["oil"]= "new and premium";
$my_car["tires"]= "new with deep treads";
unset($my_car["filth"]);
print_r($my_car);
//******************************************
$hybrid_array =[1,"hereisastring",42,True,100=>"lol",8=>"five more"];
print_r($hybrid_array);
print_r($hybrid_array);
array_push($hybrid_array,rand()); //index is at 101
print_r($hybrid_array);
echo $hybrid_array[101];

//*******************************************
$giraffe_foods = ["dip"=>"guacamole", "chips"=>"corn", "entree"=>"grilled chicken"];

$impala_foods = ["dessert"=>"cookies", "vegetable"=>"asparagus", "side"=>"mashed potatoes"];

$rat_foods = ["dip"=>"mashed earth worms", "entree"=>"trash pizza", "dessert"=>"sugar cubes", "drink"=>"lemon water"];

$potluck = $giraffe_foods+$impala_foods; // joining potluck with rat_foods would mean that drink is added. depending on which array is first, the values change
print_r($potluck); 
//*********************************************
$doge_meme = ["top_text" => "Such Python", "bottom_text" => "Very language. Wow.", "img" => "very-cute-dog.jpg", "description" => "An adorable doge looks confused."];

$bad_meme = ["top_text" => "i don't know", "bottom_text" => "i can't think of anything", "img" => "very-fat-cat.jpg", "description" => "A very fat cat looks happy."];

function createMeme($meme)
{
  $meme["top_text"]="Much PHP";
  $meme["bottom_text"]="Very programming. Wow.";
  
}

function fixMeme(&$meme)
{

}

$php_doge =createMeme($doge_meme);
print_r($php_doge);
print_r($doge_meme);
?>