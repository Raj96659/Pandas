import pandas as pd

data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "age":[22,32,41,21,31,56,78,91,17,11],
    "city":["Mah","Mah","Mum","Ben","Guj","Del","UP","TN","UTK","Ker"],
    "Salary":[1200,1300,1700,2000,900,4500,1210,2300,1000,750]
}

df = pd.DataFrame(data)

print("Updating all values of column by 5% : ")
df["Salary"] = df["Salary"] * 1.05
print(df)
