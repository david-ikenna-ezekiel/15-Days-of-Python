# pip install pandas

import pandas as pd

# Creating a simple DataFrame with two columns: 'Name' and 'Age'
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}

df = pd.DataFrame(data)

# Printing the DataFrame
print("DataFrame:")
print(df)

# Calculating the average (mean) of the 'Age' column
average_age = df['Age'].mean()
print(f"\nThe average age is: {average_age}")
