<?php
/*
Classes = Datatypes you can create yourself -> can create your own datatypes, which consist of multiple basic ones: strings, numbers, bools
school example: student datatype:
-> name
-> gpa
-> year
-> hasScholarship

can have functionality too: student example
-> hasHonors()
-> giveScholarship()
Object = instance of a class 
functions = methods of a class, initialized with the word function tho. also, to access public vars $this is needed and then an arrow to the varname; 
constructor method -> __construct(){...} -> defines an object with values at initializiation
extends -> is like the super in python: it builds a child class from the parent class
overloading a method that is inherited: just same name 
private-> you can't access the varvalue, however, it with the return of that specific error, you know it exists. functions and constructor within this class can manipulate values and print them
          inherited classes can't change it though. if you overload a method from the parent class that would change a private val, it cant do it afterwards
protected -> you can't access the var itself, but you can change it with subclasses methods. you can also print them through these methods
it probably makes sense to use these types. thorugh individual functions called getters/setters you can retrieve/set information of a class specifically. Right there, validation can be added as well.
Static vars are vars that don't change for every object. can be useful if it stays the same accross multiple objects. to access their information, scope resolution operator is used. :: -> like this: myCLASSNOTOBJECTname::staticvarname; -> 

}
*/
//First object ever in PHP wooooooooooooooOOOOOO
<?php
class StringUtilities{
  public static function str_to_lower($string)
  {
    $string = strtolower($string);
    if(strlen($string)>1)
    {
      $string[1]=strtoupper($string[1]);
    }
    return $string;
  }
}
class Pajamas {
  private $owner,$fit,$color;

  function __construct($owner, $fit, $color)
  {
    $this->owner = StringUtilities::str_to_lower($owner);
    $this->fit = $fit;
    $this->color = $color;
    echo $this->describe();
  }
  public function describe()
  {
    return "owner of this pajama: ".$this->owner ." fit: ".$this->fit ." color: ".$this->color ;
  }
  public function setFit($newSize)
  {
    $this->fit= $newSize;
  }
}

class ButtonablePajamas extends Pajamas
{
  private $button_state="unbuttoned";

  
  public function describe()
  {
    return Pajamas::describe()." your Button is: $this->button_state";
  }
  
  public function toggleButtons()
  {
    if($this->button_state ==="unbuttoned")
      $this->button_state = "buttoned";
    else
      $this->button_state = "unbuttoned";
  }
}

//$chicken_pj = new Pajamas("CHICKEN","slim","red");
//$chicken_pj->setFit("tight");
//echo $chicken_pj->describe();

$moose_PJs = new ButtonablePajamas("moose","kindalus","blue");
$moose_PJs->toggleButtons();
echo $moose_PJs->describe();



//$l1ol = StringUtilities::str_to_lower("HelloWorLD");
//echo $lol;
?>




?>