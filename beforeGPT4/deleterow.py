import pandas as pd

df = pd.read_csv('论文.csv')

df = df[df['content'].str.contains('论文')]

df.to_csv('./deleterow/论文.csv')