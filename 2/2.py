import pandas as pd

df = pd.read_csv('input', sep=' ', header=None, names=['Shape1', 'Outcome'])

df['Shape1'] = df.Shape1.map({'A': 0, 'B': 1, 'C': 2})
df['Outcome'] = df.Outcome.map({'X': 2, 'Y': 0, 'Z': 1})
df['Shape2'] = (df.Shape1 + df.Outcome) % 3

df['Points_Shape'] = df.Shape2 + 1
df['Points_Outcome'] = df.Outcome.map({2: 0, 0: 3, 1: 6})

df['Points'] = df.Points_Shape + df.Points_Outcome
df.to_csv('output', index=False)

print(df.Points.sum())

