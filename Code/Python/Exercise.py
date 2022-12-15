# %%
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
from unicodedata import normalize
import requests
import re
from datetime import datetime

data=pd.read_csv("data.csv")


# %%
#Erwthma 1
# find recycl in data['type']
year_to_tons_map = {}

for i in range(len(data)):
    if bool(re.search("Recycl[a-zA-Z]",data['type'][i])):
        date = datetime.strptime(data['date'][i], '%Y-%m-%dT%H:%M:%S.%f').year
        if date in year_to_tons_map:
            year_to_tons_map[date] += data['total_in_tons'][i]
        else:
            year_to_tons_map[date] = data['total_in_tons'][i]
            
#print(year_to_tons_map[2022])
# print(year_to_tons_map.keys)
# print(year_to_tons_map.values)


years = list(year_to_tons_map.keys())
tons = list(year_to_tons_map.values())
plt.bar(range(len(year_to_tons_map)), tons, tick_label=years)
plt.xlabel("Years")
plt.ylabel("Number of tons")
plt.title("Number of tons of recyclables in each year")
plt.show()



# %%
#Erwthma 2

type_to_tons_map = {}
for i in range(len(data)):
    if bool(re.search("Recycl[a-zA-Z]",data['type'][i])):
        type = data['type'][i]
        if type in type_to_tons_map:
            type_to_tons_map[type] += data['total_in_tons'][i]
        else:
            type_to_tons_map[type] = data['total_in_tons'][i]


# print(type_to_tons_map)
# print(type_to_tons_map.keys)
# print(type_to_tons_map.values)


type = list(type_to_tons_map.keys())
tons_1 = list(type_to_tons_map.values())
plt.bar(range(len(type_to_tons_map)), tons_1, tick_label=type)
plt.xlabel("Types")
plt.ylabel("Number of tons")
plt.title("Number of tons of recyclables in each type")
plt.show()


# %%
#Erwthma 3

month_to_tons_map = {}

for i in range(len(data)):
    if bool(re.search("Recycl[a-zA-Z]",data['type'][i])):  
        date = datetime.strptime(data['date'][i], '%Y-%m-%dT%H:%M:%S.%f').month
        if date in month_to_tons_map:
            month_to_tons_map[date] += data['total_in_tons'][i]
        else:
            month_to_tons_map[date] = data['total_in_tons'][i]
                        
#print(year_to_tons_map[2022])
# print(month_to_tons_map.keys)
# print(month_to_tons_map.values)

d = sorted(month_to_tons_map, key=month_to_tons_map.get)[::-1][0:5]

top_5_months = {}
for i in d:
    top_5_months[i] = month_to_tons_map[i]

top = list(top_5_months.keys())
tons_2 = list(top_5_months.values())
plt.bar(range(len(top_5_months)), tons_2, tick_label=top)
plt.xlabel("Top 5 Months")
plt.ylabel("Number of tons")
plt.title("Top 5 months with the most recyclables")
plt.show()



# %%
#SQL1
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="keepo",
    passwd="kappa",
    database="pythonproject",
    port=6033
)

mycursor = mydb.cursor()
# drop table if exists
mycursor.execute("DROP TABLE IF EXISTS year_to_tons")
mycursor.execute('CREATE TABLE year_to_tons (year INT NOT NULL , tons INT NOT NULL )')
for i in range(len(year_to_tons_map)):
    data = (years[i], int(tons[i]))
    mycursor.execute("INSERT INTO year_to_tons (year, tons) VALUES (%s, %s)", (data))

mydb.commit()

# %%
#SQL2
mycursor_1 = mydb.cursor()
# drop table if exists
mycursor_1.execute("DROP TABLE IF EXISTS type_to_tons")
mycursor_1.execute('CREATE TABLE `type_to_tons` (`type` VARCHAR(100) NOT NULL , `tons` INT NOT NULL )')
for i in range(len(type_to_tons_map)):
    data = (type[i], int(tons_1[i]))
    mycursor_1.execute("INSERT INTO type_to_tons (type, tons) VALUES (%s, %s)", (data))

mydb.commit()

# %%
#SQL3
mycursor_2 = mydb.cursor()
# drop table if exists
mycursor_2.execute("DROP TABLE IF EXISTS month_to_tons")
mycursor_2.execute('CREATE TABLE `month_to_tons` (`month` INT NOT NULL , `tons` INT NOT NULL )')
for i in range(len(top_5_months)):
    data = (top[i], int(tons_2[i]))
    mycursor_2.execute("INSERT INTO month_to_tons (month, tons) VALUES (%s, %s)", (data))

mydb.commit()

# %%
#export dictionary to csv
#export year_to_tons_map to csv
import csv
#Erwthma1 csv
with open('year_to_tons.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    i = 0
    writer.writerow(["","Year","Tons"])
    for key, value in year_to_tons_map.items():
        writer.writerow([i, key, value])
        i += 1

# %%
#Erwthma2 csv
with open('type_to_tons.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    i = 0
    writer.writerow(["","Type","Tons"])
    for key, value in type_to_tons_map.items():
        writer.writerow([i, key, value])
        i += 1
    

# %%
#Erwthma3 csv
with open('top_5_months.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    i = 0
    writer.writerow(["","Month","Tons"])
    for key, value in top_5_months.items():
        writer.writerow([i, key, value])
        i += 1
    


