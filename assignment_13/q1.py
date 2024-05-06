import pandas as pd
df = pd.read_csv("Used_Bikes.csv")
jaipur_ktm = df[(df['city']=='Jaipur')&(df['brand']=='KTM')]
print(jaipur_ktm)
mim_price_jaipur_ktm = jaipur_ktm['price'].min()
print(mim_price_jaipur_ktm)