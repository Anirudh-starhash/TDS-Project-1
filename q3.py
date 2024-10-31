import pandas as pd
file=pd.read_csv("repositories.csv")
map={}
for x in file['license_name']:
    if pd.isna(x):
        continue
    if x not in map:
        map[x]=0
    else:
        map[x]+=1

i=0
top_3=[]
for x in map:
    top_3.append(x)
    i+=1
    if i==3:
        break

ans=''
for val in range(len(top_3)):
    ans+=top_3[val]
    if val!=len(top_3)-1:
        ans+=','
        
print(ans)