import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

df.dropna(inplace=True)

# Группируем по городу и вычисляем среднее значение зарплаты
group = df.groupby('City')['Salary'].mean()
print(group)