import pandas as pd
'''data = {"Name":["acer","getin","hp"],
        "age":[18,23,24],
        "salary":[15000,25000,45000]}
df=pd.DataFrame(data)
print(df)'''

data1=pd.read_csv(r"C:\Users\Admin\Downloads\ecommerce.csv")
dt=pd.DataFrame(data1)
# print(dt.head(10))
# print(dt.tail(10))
# print(dt.info())
print(dt.isnull().sum())