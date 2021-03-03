import xlrd
import json
from pymongo import MongoClient

file = open("../sheets/INAMI/2021/TXT/NOMEN_ARTICLE_EXT.TXT", encoding = "ISO-8859-1")

firstLine = file.readline()
titles = firstLine.rstrip().split("|")
data = []

for line in file:
    register = {}
    lineArray = line.rstrip().split("|")
    for key in range(0,len(titles)):
        register.update({titles[key]: lineArray[key]})
    
    data.append(register)
    break

file.close()

print(json.dumps(data))

# # Open database connection
# client = MongoClient("mongodb+srv://admin:g7ssTrLn6rSO19Hx@cluster0.pd25u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.get_database("cmcm")

# table = db.livre_bleu

# # Insert data in database
# print("Saving data...")
# callback = table.insert_many(data)
# print(callback)