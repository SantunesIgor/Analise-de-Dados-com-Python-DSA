import pandas

arq = "salarios_pandas.csv"
df = pandas.read_csv(arq)
print(df.head())

print(df['Position Title'].value_counts())