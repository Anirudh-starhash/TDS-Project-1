import pandas as pd
file=pd.read_csv("users.csv")
file.sort_values(by=['created_at'],ascending=True,inplace=True)

early_5=file[:5]
ans=''
names=early_5['login']
i=0
for x in names:
   ans+=x
   i+=1
   if i!=len(names):
       ans+=','

print(ans)
    