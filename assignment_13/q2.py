import pandas as pd
df = pd.read_csv("Used_Bikes.csv")
delhi_first_owner = df[(df['owner'] == "First Owner") &(df['city']=='Delhi')]
print(delhi_first_owner)
min_age_delhi = delhi_first_owner['age'].min()
print(min_age_delhi)
max_age_delhi = delhi_first_owner['age'].max()
print(max_age_delhi)
