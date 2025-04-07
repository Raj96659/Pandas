'''
Handling Missing Data

isnull() method is used.
True : means missing
False : value present
'''

import pandas as pd

data = {
    "name":["A",None,"C","D","E","F","G","H","I","J"],
    "age":[22,None,41,21,31,56,78,91,17,11],
    "city":["Mah",None,"Mum","Ben","Guj","Del","UP","TN","UTK","Ker"],
    "Salary":[1200,None,1700,2000,900,4500,1210,2300,1000,750]
}

df = pd.DataFrame(data)

print("Check the missing values : ")
print(df.isnull())

print("\n")

print("Count the missing value in each column : ")
print(df.isnull().sum())

print("\n")

print("Drop the missing value : ")
print(df.dropna(axis=0,inplace=True))             # axis 0 means drop rows, axis 1 means drop column.

print("\n")
print("After droping")
print(df)

# Another way to handle missing value is using fillna method.

data1 = {
    "name":["A","B","C"],
    "age":[22,None,23]
}

df1 = pd.DataFrame(data1)
df1["age"].fillna(df1["age"].mean(),inplace=True)
print(df1)
