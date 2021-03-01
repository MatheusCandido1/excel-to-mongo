# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:15:41 2019

@author: Matheus
"""

import xlrd


book = xlrd.open_workbook("../sheets/Livre-Bleu/2021/livre-bleu-au-20210201.xls")


# sheet = book.sheet_by_name("new2")

# database = MySQLdb.connect(host="localhost", user = "root", passwd = "root", db = "emej")

# cursor = database.cursor()

# query = """INSERT INTO cpf_cm(cpf, ej) VALUES (%s,%s)"""

# for r in range(1, sheet.nrows):
#         cpf = sheet.cell(r,0).value 
#         ej = sheet.cell(r,1).value 

#         values = (cpf,ej)

#         cursor.execute(query, values)
        
# cursor.close()

# database.commit()

# database.close()
