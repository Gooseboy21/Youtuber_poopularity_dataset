import pandas as pd

df = pd.read_csv("new_Youtube_Data.csv")

for i in range(len(df["Country"])):
    print(df.Country[i])
    if df.Country[i] == "United States":
        
        df.Country[i] = "United States of America"

print(df)

df.to_csv("new_Youtube_Data2.csv", index = False)
