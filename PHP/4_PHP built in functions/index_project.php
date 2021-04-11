<?php
$initial = '555'; #octal number
$a = base_convert($initial,8,10);
$b = deg2rad($a);
$c = cos($b); 
$d = round($c,3);
$e = log($d);
$f = abs($e);
$g = acos($f);
$h = rad2deg($g);
$i = floor($h);
$j = $i-47;
echo $j;
?>