import pandas as pd
from datetime import datetime
file=pd.read_csv("repositories.csv")

def is_date_weekend(x):
    year,month,date=int(x[:4]),int(x[5:7]),int(x[8:10])
    dt=datetime(year,month,date)
    
    if dt.weekday() in [5,6]:
        return True
    else:
        return False
    
    

file['is_weekend']=file['created_at'].apply(is_date_weekend)

map={}
user_status=file[['login','is_weekend']]

for _,row in user_status.iterrows():
    if row['is_weekend']==True:
        if row['login'] not in map:
            map[row['login']]=1
        else:
            map[row['login']]+=1
            
data=[]
for x in map:
    data.append({
        'name':x,
        'count':map[x]
    })

data=pd.DataFrame(data)
data.sort_values(by=['count'],ascending=False,inplace=True)
top_5=data[:5]
ans=''
for _,row in top_5.iterrows():
    ans+=row['name']+','
    
ans=ans[:-1]
print(ans)