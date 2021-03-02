import xlrd
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:g7ssTrLn6rSO19Hx@cluster0.pd25u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("cmcm")

table = db.livre_bleu

book = xlrd.open_workbook("../sheets/Livre-Bleu/2021/livre-bleu-au-20210201.xls")

sheet = book.sheet_by_name("Nomenclature")

titles = []
data = []


#Print columns title
for col in range (0, sheet.ncols):
    title = sheet.cell(0,col).value
    titles.append(title)

# Print cell value
for row in range(1, sheet.nrows):
    register = []
    for col in range (0, sheet.ncols):
        cell = sheet.cell(row,col).value
        register.append({titles[col]: cell})
    data.append(register)

#print(data)
