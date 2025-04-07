import pandas as pd

df_customer = pd.DataFrame({
    'custid':[1,2,3],
    'Name':['A','B','C']
})

df_orders = pd.DataFrame({
    'custid':[4,5],
    'Name':['D','E']
})

df_concat = pd.concat([df_customer,df_orders],ignore_index=True)
print(df_concat)
