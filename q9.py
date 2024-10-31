import pandas as pd
file=pd.read_csv("users.csv")

corr=file['followers'].corr(file['public_repos'])
print(corr)