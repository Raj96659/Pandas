import pandas as pd

data = {
    "name":["Raj","Jay"],
    "age":[22,21]
}

df = pd.DataFrame(data)
print(df)

# to save the file
df.to_csv("Z_Cleaned_CSV",index=False)
