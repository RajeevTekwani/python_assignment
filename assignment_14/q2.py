import pandas as pd
df = pd.read_csv("laptopPrice.csv")
group = df.groupby("processor_brand")
group1=group[["processor_brand"]].value_counts()
print(group1)
print("max available brand is :",group1.idxmax())
print("min available brand is :",group1.idxmin())

