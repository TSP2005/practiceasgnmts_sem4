import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 17, 22, 30],
        'Salary': [50000, 1000, 60000, 75000]}

df = pd.DataFrame(data)
cleandf = df[(df['Age'] >= 18) & (df['Salary'] >= 0)]
print(cleandf)
