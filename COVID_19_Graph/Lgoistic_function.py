import numpy as np
from matplotlib import pyplot as plt
import json
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def logistic_function(x,a=1,b=0,c=1,d=0):
    return a/(1+np.exp(-c*(x-d)))+b

def fit_data_to_function(x,y,function):
    params,_ = curve_fit(function,x,y)
    plt.plot(x,y,".",label="Observations")
    y_fit = function(x,*params) 
    print(r2_score(y,y_fit))
    plt.plot(x,y_fit,label="Fitted Curve")
    plt.legend()
    plt.show()
    return params

def plateau(x,y,params,function,diff = 10):
    confirmed_now = y[-1]
    confirmed_then = y[-2]
    days = 0
    while confirmed_now - confirmed_then>diff:
        days+=1
        confirmed_then = confirmed_now
        confirmed_now = function(confirmed_now+days,*params)
    
    return days,confirmed_now
    

path_additions= "COVID_19_Graph\\"
with open(path_additions+"COVID_cases.json","r") as file:
    data = json.load(file)
    
list = data["records"]
AUT_reverse_cases = []
AUT_total_cases = []
for x in list:
    if x["countriesAndTerritories"] == "Austria":
        AUT_reverse_cases.append(x["cases"])
AUT_cases = reversed(AUT_reverse_cases)
for x in AUT_cases:
    if AUT_total_cases ==[]:
        AUT_total_cases.append(int(x))
    else:
        AUT_total_cases.append(int(x)+int(AUT_total_cases[-1]))

IT_reverse_cases = []
IT_total_cases = []
for x in list:
    if x["countriesAndTerritories"] == "Italy":
        IT_reverse_cases.append(x["cases"])
IT_cases = reversed(IT_reverse_cases)
for x in IT_cases:
    if IT_total_cases ==[]:
        IT_total_cases.append(int(x))
    else:
        IT_total_cases.append(int(x)+int(IT_total_cases[-1]))

US_reverse_cases = []
US_total_cases = []
for x in list:
    if x["countriesAndTerritories"] == "United_States_of_America":
        US_reverse_cases.append(x["cases"])
US_cases = reversed(US_reverse_cases)
for x in US_cases:
    if US_total_cases ==[]:
        US_total_cases.append(int(x))
    else:
        US_total_cases.append(int(x)+int(US_total_cases[-1]))

COVID_Data = {}
COVID_Data["Austria"] = AUT_total_cases
COVID_Data["Italy"] = IT_total_cases[20:]
COVID_Data["USA"]=US_total_cases

y = COVID_Data["Austria"]
print(y)
x = np.arange(len(y))
diff =5
params = fit_data_to_function(x,y,logistic_function)
days,confirmed = plateau(x,
                         y,
                         params,
                         logistic_function,
                         diff=diff)
print(f"in {days} days until growth is less than {diff}")
#confirmed=logistic_function(x+10,*params)
print(f"Number of cases is {confirmed} in 5 days")
#print(COVID["Italy"])
        
#print(data.keys())
