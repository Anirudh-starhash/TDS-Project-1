import pandas as pd
file=pd.read_csv("users.csv")
map={}
for x in file['company']:
    if pd.isna(x):
        continue
    if x not in map:
        map[x]=0
    else:
        map[x]+=1

max=-1
name=''

for x in map:
    if map[x]>max:
        max=map[x]
        name=x
        
print(name,max)