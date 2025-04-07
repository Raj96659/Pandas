import pandas as pd

data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "age":[22,32,41,21,31,56,78,91,17,11],
    "city":["Mah","Mah","Mum","Ben","Guj","Del","UP","TN","UTK","Ker"]
}

df = pd.DataFrame(data)
print(df)

print("\n")

print('Selecting Single Column : ')
print(df["city"])

print("\n")

print("Selecting multiple column : ")
print(df[["city","age"]])

print("\n")

print("Filtering based on single column : ")
print(df[df["age"]>30])

print("\n")

print("Filtering based on multiple column : ")
print(df[(df["age"]>30) & (df["city"]=="Mah")])
