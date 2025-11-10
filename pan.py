import pandas as pd
# Create a Series from a list
numbers = [10, 20, 30, 40, 50]
series1 = pd.Series(numbers)

print("Series 1:")
print(series1)


series2 = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries 2 with Custom Index:")
print(series2)


print("\nAddition of series1 + 5:\n", series1 + 5)
print("Series1 multiplied by 2:\n", series1 * 2)
print("Mean of series1:", series1.mean())
print("Median of series1:", series1.median())




data = {
    'Name': ['Amit', 'Priya', 'Ravi', 'Neha', 'Kiran'],
    'Age': [22, 24, 23, 21, 25],
    'Marks': [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nDataFrame Info:")
print(df.info())

print("\nDataFrame Description (Statistics):")
print(df.describe())


print("\nAccess 'Name' column:")
print(df['Name'])

print("\nAccess first two rows:")
print(df.head(2))


df['Grade'] = ['B', 'A', 'C', 'B+', 'A+']
print("\nDataFrame after adding 'Grade' column:")
print(df)


df.loc[2, 'Marks'] = 80
print("\nUpdated DataFrame after changing Ravi's marks:")
print(df)


df.drop('Grade', axis=1, inplace=True)
print("\nDataFrame after deleting 'Grade' column:")
print(df)


sorted_df = df.sort_values(by='Marks', ascending=False)
print("\nDataFrame sorted by Marks (descending):")
print(sorted_df)
