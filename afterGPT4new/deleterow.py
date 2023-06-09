import pandas as pd

df = pd.read_csv('./origin/copilot_office.csv')

df = df[df['content'].str.contains('copilot', case=False) & df['content'].str.contains('office', case=False)]

df.to_csv('./deleterow/copilot_office.csv')