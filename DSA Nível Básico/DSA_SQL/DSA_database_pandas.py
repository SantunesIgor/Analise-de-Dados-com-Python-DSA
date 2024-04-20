import pandas as pd
import sqlite3

con = sqlite3.connect('Archives/cap12_dsa.db')
cursor = con.cursor()

print('---------------')
query = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query)
data = cursor.fetchall()
for i in data:
    print(i)

print('---------------')
print(type(data))

print('---------------')
df = pd.DataFrame(data, columns = ['ID_Pedido',
                                   'ID_Cliente',
                                   'Nome_Produto',
                                   'Valor_Unitário',
                                   'Unidades_Vendidas',
                                   'Custo'])
print(df.head(5))
cursor.close()
con.close()

print('---------------')
mean_Unidades_Vendidas = df['Unidades_Vendidas'].mean()
print(type(mean_Unidades_Vendidas))
print(mean_Unidades_Vendidas)

print('---------------')
mean_Unidades_Vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(mean_Unidades_Vendidas_por_produto.head(10))

print('---------------')
df1 = df[df['Valor_Unitário'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(df1)

print('---------------')
df2 = df[df['Valor_Unitário'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
print(df2)

print('---------------')
df2 = df[df['Valor_Unitário'] > 199].groupby('Nome_Produto') \
                                    .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                                    .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(df2)