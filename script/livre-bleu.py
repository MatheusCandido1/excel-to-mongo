import xlrd
from pymongo import MongoClient

book = xlrd.open_workbook("../sheets/Livre-Bleu/2021/livre-bleu-au-20210201.xls")

sheet = book.sheet_by_name("Nomenclature")

titles = []
data = []


#Print columns title
for col in range (0, sheet.ncols):
    columnName = sheet.cell(0,col).value
    title = columnName.replace(" ", "_").replace("-", "_").lower()
    titles.append(title)

# Print cell value
for row in range(1, sheet.nrows):
    register = {}
    for col in range (0, sheet.ncols):
        cell = sheet.cell(row,col).value
        register.update({titles[col]: cell})
    data.append(register)

print(data)

# # Open database connection
# client = MongoClient("mongodb+srv://admin:g7ssTrLn6rSO19Hx@cluster0.pd25u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.get_database("cmcm")

# Count data in database
#count = table.count_documents({});
#print(count);

# Count data in database
#count = table.count_documents({});
#print(count);

# Insert data in database
#print("Saving data...")
#callback = table.insert_many(data)
#print(callback)
