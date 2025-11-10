import pandas as pd
data = [
    ['Alice', 25, 'Mumbai'],
    ['Bob', 30, 'Delhi'],
    ['Charlie', 22, 'Pune']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
