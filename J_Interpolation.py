# Refer Link
# https://chatgpt.com/share/67f3a207-d584-800b-bb59-edbcd24c8f20


import pandas as pd

data = {
    "name":["A","B","C","D","E","F"],
    "age":[28,None,22,29,30,32],
    "Salary":[50000,None,45000,52000,49000,70000],
    "Per_Score":[85,None,78,92,88,95]
}

df = pd.DataFrame(data)

df.interpolate(method="linear",axi=0,inplace=True)

print(df)
