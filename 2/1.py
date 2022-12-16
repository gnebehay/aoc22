import pandas as pd

def outcome(row):

    if (row.Shape1 == 'A' and row.Shape2 == 'B') or \
       (row.Shape1 == 'B' and row.Shape2 == 'C') or \
       (row.Shape1 == 'C' and row.Shape2 == 'A'):
           return 6

    if row.Shape1 == row.Shape2:
        return 3

    return 0

df = pd.read_csv('input', sep=' ', header=None, names=['Shape1', 'Shape2'])

df['Shape2'] = df.Shape2.map({'X': 'A', 'Y': 'B', 'Z': 'C'})

df['Points_Shape'] = df.Shape2.map({'A': 1, 'B': 2, 'C': 3})
df['Points_Outcome'] = df.apply(outcome, axis=1)

df['Points'] = df.Points_Shape + df.Points_Outcome
df.to_csv('output', index=False)

print(df.Points.sum())

