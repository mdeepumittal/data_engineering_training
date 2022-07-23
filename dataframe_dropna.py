import pandas as pd
df=pd.read_csv('sample_file.csv')
copy=pd.read_csv('sample_file.csv')
copy["null columm"] = None

print(df)
print(copy)
print (len(df),len(copy))
copy.dropna(axis=0,how="any",inplace=True)
print(copy)