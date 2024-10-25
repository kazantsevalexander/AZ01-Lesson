import pandas as pd

df = pd.read_csv('Spotify Most Streamed Songs.csv')

print(df.head())

print(df.info())

print(df.describe())