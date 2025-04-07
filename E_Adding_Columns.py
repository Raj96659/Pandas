import pandas as pd

data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "age":[22,32,41,21,31,56,78,91,17,11],
    "city":["Mah","Mah","Mum","Ben","Guj","Del","UP","TN","UTK","Ker"]
}

df = pd.DataFrame(data)
print(df)

print("\n")

print("Adding Columns : ")
df["Salary"] = [12000,25000,32000,2000,4000,1250,100,250,800,850]
print(df)

print("\n")

print("Adding column using insert method : ")
#df.insert(loc,column_name,some_data)
df.insert(0,"EmpID",[101,102,103,104,105,106,107,108,109,110])
print(df)

