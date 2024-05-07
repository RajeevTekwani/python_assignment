import pandas as pd
df = pd.read_csv("laptopPrice.csv")
group = df.groupby("brand")
apple_data = group.get_group('APPLE')
apple_data1 = apple_data.sort_values(by="Price",ascending=False)
print(apple_data1.head(5))
print(apple_data1.tail(5))