import pandas as pd

data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "age":[22,32,41,21,31,56,78,91,17,11],
    "city":["Mah","Mah","Mum","Ben","Guj","Del","UP","TN","UTK","Ker"]
}

df = pd.DataFrame(data)
print(df)

print("\n")

print("First 5 rows : ")
print(df.head())

print("\n")

print("Last 5 rows : ")
print(df.tail())

print("\n")

print("Display info of dataset : ")
print(df.info())

print("\n")

print("Describe the dataset : ")
print(df.describe())

print("\n")

print("Shape of dataset : ")
print(df.shape)

print("\n")

print("Columns : ")
print(df.columns)
