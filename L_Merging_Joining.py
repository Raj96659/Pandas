import pandas as pd

df_customer = pd.DataFrame({
    'custid':[1,2,3],
    'Name':['A','B','C']
})

df_orders = pd.DataFrame({
    'custid':[1,2,4],
    'orderamount':[200,250,120]
})

df_merge = pd.merge(df_customer,df_orders,on='custid',how='inner')
print(df_merge)

print("\n")

df_merge = pd.merge(df_customer,df_orders,on='custid',how='outer')
print(df_merge)
