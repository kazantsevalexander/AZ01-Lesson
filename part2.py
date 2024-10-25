import pandas as pd

df = pd.read_csv('dz.csv')
df.fillna(0, inplace=True)

# Фильтруем строки, где Salary > 0
df_filtered = df[df['Salary'] > 0]

print(df)

group = df.groupby('City')['Salary'].mean()
print(group)