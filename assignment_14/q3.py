import pandas as pd
df = pd.read_csv("laptopPrice.csv")
group = df.groupby("processor_brand")
df1 =group["Price"].agg(minimum_price = "min",maximum_price = "max")
print(df1)
