# IN THIS FIEL WE WILL LEARN ABOUT PANDAS DATAFRAME 

'''
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
'''

import pandas as pd

data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'],  # CREATING A DATAFRAME
        'Age' : [24, 27, 22, 32],
        'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3", "Employee 4"]) # DISPLAYING THE DATAFRAME
# print(df)

# print(df.loc["Employee 2"])  # ACCESSING A ROW BY LABEL
# print(df.iloc[2])  # ACCESSING A ROW BY POSITION
# print(df['Name'])  # ACCESSING A COLUMN BY LABEL
# print(df.iloc[:, 1])  # ACCESSING A COLUMN BY POSITION


# Add a new column

df['Salary'] = [70000, 80000, 60000, 90000] # ADDING A NEW COLUMN TO THE DATAFRAME
df['Department'] = ['HR', 'Finance', 'IT', 'Marketing']


#Add a new rows

new_rows = pd.DataFrame([{'Name': 'Eve', 'Age': 29, 'City': 'Miami', 'Salary': 75000, 'Department': 'Sales'},
                       {'Name': 'James', 'Age': 31, 'City': 'Boston', 'Salary': 82000, 'Department': 'IT'}], index = ['Employee 5', 'Employee 6'])
df = pd.concat([df, new_rows]) # CONCATENATING THE NEW ROWs TO THE EXISTING DATAFRAME
print(df)

