
from selenium import webdriver
import time
import re
from datetime import datetime
import smtplib
#import pandas as pd

# prev_data = open("log.txt","r")
# print(prev_data)
# data=[]
# for i in prev_data:
#     data.append(i.split(" "))
# print(data)
# exit()

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome("Coronavirus_Email_Project\\chromedriver.exe")
        # self.driver = webdriver.Chrome("chromedriver.exe")
        return None

         

    def get_data(self,Country):

        try:
            #Receiving Data
            self.driver.get('https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/')
            print("I work")
            table = self.driver.find_element_by_xpath('//*[@id="table3"]/tbody[1]')
            new_table=table.text.split("\n")

            print("I imported the table as fast as I could!")
            self.driver.close()
            
            #Creating Variables
            #Previous_Day Variables
            #11.03: Removed Date from prev. data
            Previous_data_exists=False
            prev_continents_cases = {"Europe":0,"Africa":0, "Australia/Oceania":0,"Asia":0,"caribbean":0,"North America":0,"South America":0}
            prev_continents_deaths = {"Europe":0,"Africa":0, "Australia/Oceania":0,"Asia":0,"caribbean":0,"North America":0,"South America":0}
            prev_Country_Cases = 0
            prev_Country_Deaths= 0
            prev_rates = open("Coronavirus_Email_Project\\Cases.txt","r").read().split(" ")
            prev_new_infections_global = int(prev_rates[0])
            prev_new_infections_local = int(prev_rates[1])
            
                #The table will be saved in a text file. This way, we can calculate the variables with a function
                #There will be another file created for analysis with the same content, but with a date added. Perhaps we can edit the for loops and add it at the end of the file
            try:
                prev_data = open("Coronavirus_Email_Project\\prev.txt","r").read().split("\n")
                Previous_data_exists=True
                #prev_data_backup = 

            except: 
                print("Previous Data could not be read!")
                if(input("Continue anyway? [y/n]")=="n"):
                    if(input("Do you want to create a new previous file with the current data? [y/n]")=="y"):
                        prev_data = open("log.txt","r+")
                        for i in new_table:
                            prev_data.write(i+"\n")
                        print("File Created in current directory of Terminal.")
                        print("Exiting...")
                        prev_data.close()
                        time.sleep(3)
                        exit()
                    
            #exit()

            #Current variables
            Date=datetime.date(datetime.now())
            continents_cases = {"Europe":0,"Africa":0, "Australia/Oceania":0,"Asia":0,"caribbean":0,"North America":0,"South America":0}
            continents_deaths = {"Europe":0,"Africa":0, "Australia/Oceania":0,"Asia":0,"caribbean":0,"North America":0,"South America":0}
            Country_Cases = 0
            Country_Deaths =0
            
            #Calculated datavariables
            new_infections_global=0
            new_deaths_global =0
            new_infections_local=0
            new_deaths_local =0
            Growthfactor_global=0
            Growthfactor_local=0

            
            #Evaluation of data
            #inserting Data into variables
            Country_Cases,Country_Deaths = Evaluation(new_table,continents_cases,continents_deaths,Country_Cases,Country_Deaths,Country)
            if(Previous_data_exists):
                prev_Country_Cases,prev_Country_Deaths = Evaluation(prev_data,prev_continents_cases,prev_continents_deaths,prev_Country_Cases,prev_Country_Deaths,Country)
            
                       
            #Calculations 
            prev_cases_global = sum(prev_continents_cases.values())
            prev_deaths_global = sum(prev_continents_deaths.values())
            global_cases = sum(continents_cases.values())
            global_deaths = sum(continents_deaths.values())
            #Global Cases and deaths
            new_infections_global = global_cases - prev_cases_global
            new_deaths_global = global_deaths - prev_deaths_global
            Growthfactor_global = new_infections_global/prev_new_infections_global
            mortalitiyrate_global = new_deaths_global/global_cases * 100
            #Local Cases and deaths
            new_infections_local = Country_Cases - prev_Country_Cases
            new_deaths_local = Country_Deaths - prev_Country_Deaths
            Growthfactor_local = new_infections_local / prev_new_infections_local
            mortalitiyrate_local = Country_Deaths / Country_Cases * 100

            if(input("Evaluation complete. Do you wish to update the previous data? [y/n] ") == "n"):
                update = False
            else:
                update= True
            print("I evaluated the data :)")
            #row = country_element.find_element_by_xpath("./..")
            
            #data_spaced = data.splt(" ")
            print("Now I'll print the data :)")

            #The Formula needs to be done. it is based on this video: https://www.youtube.com/watch?v=Kas0tIxDvrg
            #The Virus Growth behaves exponentially. it can be described with the formula:
            #deltaNd = E * p * Nd  | Nd + 1 = E * p * Nd + Nd  -->  Nd = (1 + E* p)^d * N0
            
            #Nd = Number of cases on a given day
            #E = Average number of people exposed to infected person each day
            #p = probability exposure becomes an infection
            #since these Factors can only be manipulated by precautions like washing hands or exposure to infected people, the growthrate E*p can be calculated by  

            # Meaning the Equation would be like this: Nd +1 = (1+I)*Nd
            #maybe creating a log file with the date
         
            Output_string =""
            Output_string +=("Date: "+str(Date))
            Output_string +=("\n\n")

            Output_string +=("--- Local Data ---\n")
            Output_string +=("Country: " + Country)
            Output_string +=("\n")
            Output_string +=("Local total cases: {:,}".format(Country_Cases).replace(",","."))
            Output_string +=("\n")
            Output_string +=("Local total deaths: {:,}".format(Country_Deaths).replace(",","."))
            Output_string +=("\n")
            
            Output_string +=("New cases: {:,}".format(new_infections_local,).replace(",","."))
            Output_string +=("\n")
            Output_string +=("New Deaths: {:,}".format(new_deaths_local).replace(",","."))
            Output_string +=("\n")
            Output_string +=("Growthrate local: {:.2f} %".format(Growthfactor_local).replace(".",","))
            Output_string +=("\n")
            Output_string +=("Mortalityrate local: {:.2f} %".format(mortalitiyrate_local).replace(".",","))
            Output_string +=("\n")
            Output_string +=("\n")

            Output_string +=("--- Global Data ---\n")
            Output_string +=("Total cases globally: {:,}".format(global_cases).replace(",","."))
            Output_string +=("\n")
            Output_string +=("Total deaths globally: {:,}".format(global_deaths).replace(",","."))
            Output_string +=("\n")
            Output_string +=("New cases: {:,}".format(new_infections_global).replace(",","."))
            Output_string +=("\n")
            Output_string +=("New deaths: {:,}".format(new_deaths_global).replace(",","."))
            Output_string +=("\n")
            Output_string +=("Growthrate global: {:.2f}%".format(Growthfactor_global).replace(".",","))
            Output_string +=("\n")
            Output_string +=("Mortalitiyrate global: {:.2f}%".format(mortalitiyrate_global).replace(".",","))

            print(Output_string)

            #Creating files and backups
            if(update):
                log_file = open("Coronavirus_Email_Project\\log.txt","w")
                log_file.write("Date: {} _ LC: {} _ NLC: +{} _ LDs: {} _ NLD: +{} _ G: {} _ GC: {} _ NGC: +{} _ GD: {} _ NGD: +{} _ G: {} ".format(Date,Country_Cases,new_infections_local,Country_Deaths,new_deaths_local,Growthfactor_local,global_cases,new_infections_global,global_deaths,new_deaths_global,Growthfactor_global))
                log_file.close()
                backup_prev_file= open("Coronavirus_Email_Project\\prev_backup.txt","w")
                Writing_to_file(backup_prev_file,prev_data)
                backup_prev_file.close()
                prev_file = open("Coronavirus_Email_Project\\prev.txt","w")
                Writing_to_file(prev_file,new_table)
                prev_file.close()
                backup_Cases_file = open("Coronavirus_Email_Project\\Cases_backup.txt","w")
                backup_Cases_file.write("{} {}".format(prev_new_infections_global, prev_new_infections_local))
                backup_Cases_file.close()
                Cases_file = open("Coronavirus_Email_Project\\Cases.txt","w")
                Cases_file.write("{} {}".format(new_infections_global,new_infections_local))
                Cases_file.close()

            #the mail function
            #send_mail(country_element.text, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical)

            #self.driver.close()
        except:
            print("failed!")
            self.driver.quit()
'''
    def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('email', 'password')

        subject = 'Coronavirus stats in your country today!'

        body = 'Today in ' + country_element + '\
            \nThere is new data on coronavirus:\
            \nTotal cases: ' + total_cases +'\
            \nNew cases: ' + new_cases + '\
            \nTotal deaths: ' + total_deaths + '\
            \nNew deaths: ' + new_deaths + '\
            \nActive cases: ' + active_cases + '\
            \nTotal recovered: ' + total_recovered + '\
            \nSerious, critical cases: ' + serious_critical  + '\
            \nCheck the link: https://www.worldometers.info/coronavirus/'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'Coronavirus',
            'email',
            msg
        )
        print('Hey Email has been sent!')

        server.quit()
'''

def Writing_to_file(filey,data1):
    for i in data1:
        if(i == data1[-1]):
            filey.write(i)
        else:
            filey.write(i+"\n")

def Evaluation(new_table,continents_cases,continents_deaths,Country_Cases,Country_Deaths,Country):
    for country_full_data in new_table:
        data = country_full_data.split(" ")
        if(len(data)<5):
            continents_cases[""+data[3]+""] += int(data[1].replace(",",""))
            continents_deaths[""+data[3]+""] += int(data[2].replace(",",""))
            if(data[0] == Country):
                Country_Cases = int(data[1].replace(",",""))
                Country_Deaths = int(data[2].replace(",",""))
        else:
            Data_Country = ""
            Data_Continent =""
            Continent= False
            Cases = 0
            Deaths = 0
            for i in range(len(data)):
                try:
                    if(Cases == 0):
                        Cases = int(data[i].replace(",",""))
                    elif(Deaths == 0):
                        Deaths = int(data[i].replace(",",""))
                    Continent = True
                    int(data[i].replace(",",""))
                except:
                    if(Continent):
                            Data_Continent +=data[i]
                            Data_Continent += " "
                    else:
                        Data_Country += data[i]
                        Data_Country += " "
            Data_Country = Data_Country.strip()
            Data_Continent = Data_Continent.strip()
            continents_cases[""+Data_Continent+""] += Cases
            continents_deaths[""+Data_Continent+""] += Deaths
            if(Data_Country == Country):
                Country_Cases = Cases
                Country_Deaths = Deaths
    return Country_Cases,Country_Deaths



Country = "Austria" 
bot = Coronavirus()
bot.get_data(Country)
