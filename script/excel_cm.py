# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:15:41 2019

@author: Matheus
"""

import xlrd


book = xlrd.open_workbook("../sheets/Livre-Bleu/2021/livre-bleu-au-20210201.xls")


sheet = book.sheet_by_name("Nomenclature")

titles = []
data = []

# database = MySQLdb.connect(host="localhost", user = "root", passwd = "root", db = "emej")

# cursor = database.cursor()

# query = """INSERT INTO cpf_cm(cpf, ej) VALUES (%s,%s)"""

# Print columns title
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

print(data)
#         cursor.execute(query, values)
        
# cursor.close()

# database.commit()

# database.close()
