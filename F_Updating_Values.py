import pandas as pd

data = {
    "name":["A","B","C","D","E","F","G","H","I","J"],
    "age":[22,32,41,21,31,56,78,91,17,11],
    "city":["Mah","Mah","Mum","Ben","Guj","Del","UP","TN","UTK","Ker"]
}

df = pd.DataFrame(data)

print("Updating value : ")
# df.loc[row_index,column_name] = new_value
df.loc[0,"age"] = 23
print(df)

