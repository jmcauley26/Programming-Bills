# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 18:37:15 2019

@author: jmcau
"""
import sys
import pandas as pd 
import csv
import numpy as np

rawdata = pd.read_csv('bills.csv', names = ["Company", "Account Name","Year", "Month", "Day", "Value","Type"])

data = pd.read_csv('bills.csv', names = ["Company", "Account Name","Year", "Month", "Day", "Value","Type"]) 
data['Date'] = data['Year'].astype(str) + "/" + data['Month'].astype(str) + "/" + data['Day'].astype(str)

data['Type2'] = data['Type'].replace(" credit", "credit").replace() 
data['Type3'] = data['Type2'].replace(" debit", "debit").replace() 

data['Date']=pd.to_datetime(data['Date'])

def read_bills2():
    print(rawdata)
    print()
    display_menu()

def yearval(msg):
    while True:
        try:
            yearval = int(input(msg))  
            if 2000 > yearval or 2020 < yearval:
            #if 2020 < yearval:
                print("Invalid Year!")
                continue
            return yearval
        except ValueError:
            print("Incorrect Format - Try Again with a number!.")
            continue
        else:
            return yearval 
            break
        
def monthval(msg):
    while True:
        try:
            monthval = int(input(msg))  
            if 12 < monthval or 0 >= monthval:
                print("Invalid Month!")
                continue
            return monthval
        except ValueError:
            print("Incorrect Format - Try Again with a number!.")
            continue
        else:
            return monthval 
            break
        
def dayval(msg):
    while True:
        try:
            dayval = int(input(msg))  
            if 31 < dayval or 0 >= dayval:
                print("Invalid Day!")
                continue
            return dayval
        except ValueError:
            print("Incorrect Format - Try Again with a number!.")
            continue
        else:
            return dayval 
            break

def insert_bill():
    with open('bills.csv','a') as f:
        
        writer=csv.writer(f)
    
        input1 = str(input("Enter a Company: "))
        input2 = str(input("Enter a Name: "))
        input3 = yearval("Enter a Year: ")
        input4 = monthval("Enter a Month (1-12): ")
        input5 = dayval("Enter a Day (1-31): ")
        input6 = float(input("Enter an Amount: "))
        input7 = str(input("Debit or Credit?: "))
        
        writer.writerow([input1,input2,input3,input4,input5,input6,input7])
        
    print()    
    print('Thank you - the bill has now been added')
    
def welcome():
    print('Hi and Welcome to the Bill Utility Company!')
    
def reports_menu():
    choice = input("""    A: Bills by Date
    B: Total # of Bills
    C: Most Popular Provider
    D: Max Bills
    E: Time Bills
    F: Total by Years
    G: Average spend per period

    Please select a Report: """)
    
    if choice =="a":
        report_bydate()
    elif choice =="b":
        bills_totalnumber()
    elif choice =="c":
        bills_mostcommon()
    elif choice =="d":
        max_bills()
    elif choice =="e":
        time_betweenbills()
    elif choice =="f":
        total_byyears()
    elif choice =="g":
        avgspend_perperiod()
    
    display_menu()
    
def report_bydate():

    data['Date']=pd.to_datetime(data['Date'])
    datedata = data.sort_values(by=['Date'])
    
    print()
    print('*Bills in Date Order*')
    print()
    print(datedata)
    
def bills_totalnumber():
    
    print(" ")
    print("The totel number of bills in the system is")
    print(len(data))
    
def bills_mostcommon():
    
    print(" ")
    popular = data['Company'].value_counts().idxmax()
    print("The most popular provider is" + " " + popular)
    
def max_bills():
    
    #print(data)
    #print(data[['Type']][data.Value == data.Value.max()])
    
    #print(data['Value'].max())
    
    print(data.groupby(['Type3'], sort=False)['Value'].max())
    
def avgspend_perperiod():
    
    data["Year"] = int(input("Select a Year: "))
    data["Month"] = int(input("Select a Month: "))
    
    grouping = data.groupby(["Year", "Month"])

    monthly_averages = grouping.aggregate({"Value":np.mean})

    print(monthly_averages)
    
def time_betweenbills():
    
    datedata2 = data.sort_values(by=['Date'])
    datedata2['new'] = datedata2['Date'] - datedata2['Date'].shift(1)
    print(datedata2)
    
def total_byyears():
    
    #print(data.groupby(['Year'], sort=False)['Type'].max())
    
    print(data.groupby(['Year', 'Type3'])['Value'].sum())
        
def display_menu(): 
    choice = input("""    A: View Bills
    B: Insert a Bill
    C: Produce Reports
    Q: Quit/Log Out

    Please enter your choice: """)

    if choice =="a":
        read_bills2()
    elif choice =="b":
        insert_bill()
    elif choice =="c":
        reports_menu()
    elif choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C,D or Q.")
        
        display_menu()           

def main():
    welcome()
    display_menu()
    
if __name__ == '__main__':
    main()