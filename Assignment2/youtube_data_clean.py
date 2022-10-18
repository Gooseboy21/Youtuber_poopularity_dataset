from unittest import skip
import pandas as pd

df = pd.read_csv("new_Youtube_Data.csv")

for i in range(len(df["Country"])):
    if type(df["Country"][i]) == "United States":
        print("hello")
        df["Country"][i] = "United States of America"


print("hello")
print(df)

#df.to_csv("new_Youtube_Data2.csv", index = False)





""""

for value in df.avgViews:
    if value[-1] == 'K':
        value = value[:-1]
        #value *= 1000
        #print(value)
        

#print(df.avgViews)

def number_conversion(number):
    if number[-1] == "M":
        number = float(number[:-1])
        number *= 1000000

    elif number[-1] == "K":
        number = float(number[:-1])
        number *= 1000
    return number

print(df['avgViews'][0])


for i in range(len(df["avgViews"])):
    if type(df.avgViews[i]) == float:
        continue
    else:
       df.avgViews[i] = number_conversion(df.avgViews[i])

for i in range(len(df.avgLikes)):
    if type(df.avgLikes[i]) == float:
        continue
    else:
       df.avgLikes[i] = number_conversion(df.avgLikes[i])

for i in range(len(df["Avg Comments"])):
    if type(df["Avg Comments"][i]) == float:
        continue
    else:
       df["Avg Comments"][i] = number_conversion(df["Avg Comments"][i])  

for i in range(len(df["Subscribers"])):
    if type(df["Subscribers"][i]) == float:
        continue
    else:
       df["Subscribers"][i] = number_conversion(df["Subscribers"][i])


"""



