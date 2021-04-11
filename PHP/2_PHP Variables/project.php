<?php
  $riel = 2103942;
  $kyat = 19092;
  $krones = 109;
  $lek = 9094;
  $exchangerate_riel = 0.00026;
  $exchangerate_kyat = 0.00066;
  $exchangerate_krones = 0.11;
  $exchangerate_lek = 0.0090;
  echo "Starting money riel: $riel\n";
  echo "Starting money kyat: $kyat\n";
  echo "Starting money krones: $krones\n";
  echo "Starting money lek: $lek\n";
  echo "\n";
  echo "money riel: $riel in USD: ".$riel*$exchangerate_riel."\n";
  echo "money kyat: $kyat in USD: ".$kyat*$exchangerate_kyat."\n";
  echo "money krones: $krones in USD: ".$krones*$exchangerate_krones."\n";
  echo "money lek: $lek in USD: ".$lek*$exchangerate_lek."\n";
  $total = $riel*$exchangerate_riel +$kyat*$exchangerate_kyat + $krones*$exchangerate_krones + $lek*$exchangerate_lek;
  $total -=4;
  round($total,2,PHP_ROUND_HALF_UP); #function to round answer. you could do it with modulo as well, but yeah. that's quicker sorry. 
  echo "After transaction fees: $total";
  
?>
  