import pandas as pd
df = pd.read_csv("laptopPrice.csv")
print(df.head(5))
print(df.tail(5))
print(df.shape)