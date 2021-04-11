<?php
  
$annualExpenses = [
    "vacations" => 1000,
    "carRepairs" => 1000,    
];

$monthlyExpenses = [
    "rent" => 1500,
    "utilities" => 200,
    "healthInsurance" => 200
];

$grossSalary = 48150;
$socialSecurity = $grossSalary * .062;

$incomeSegments = [[9700, .88], [29775, .78], [8675, .76]];


$totalSalary =0;
foreach ($incomeSegments as $segment)
{
  $totalSalary += $segment[0]*$segment[1];
}
print($totalSalary);
print("\n");
$afterSocialSecurity=$totalSalary-$socialSecurity;
print($afterSocialSecurity);
print("\n");
$afterAnnualExpenses=$afterSocialSecurity-$annualExpenses["vacations"]-$annualExpenses["carRepairs"];
print($afterAnnualExpenses);
$monthlyIncome=$afterAnnualExpenses/12;
print("\n");
print($monthlyIncome);
foreach($monthlyExpenses as $expense)
{
  $monthlyIncome -=$expense;
}
print("\n");
print($monthlyIncome);
$weeklyIncome = $monthlyIncome/4.33;
print("\n");
print($weeklyIncome);
$weeklyExpenses =["gas"=>25,"food"=>90,"entertainment"=>47];
foreach($weeklyExpenses as $expense)
{
  $weeklyIncome -=$expense;
}
$savings = $weeklyIncome*52;
print("\n".$weeklyIncome."\n".$savings);
