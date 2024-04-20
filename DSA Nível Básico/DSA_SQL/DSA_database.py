import sqlite3
import pandas as pd

con = sqlite3.connect('Archives/cap12_dsa.db')
cursor = con.cursor()
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
print(cursor.fetchall())

print('---------------')
query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)
nomes_colunas = [description[0] for description in cursor.description]
print(nomes_colunas)
for i in cursor.fetchall():
    print(i)

print('---------------')
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
for i in cursor.fetchall():
    print(i)

print('---------------')
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'
cursor.execute(query3)
for i in cursor.fetchall():
    print(i)

print('---------------')
query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""
cursor.execute(query4)
for i in cursor.fetchall():
    print(i)

print('---------------')
query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""
cursor.execute(query5)
for i in cursor.fetchall():
    print(i)

cursor.close()
con.close()