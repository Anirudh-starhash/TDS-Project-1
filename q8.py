import pandas as pd
file=pd.read_csv('users.csv')
login_followers_following=file[['login','followers','following']]
print(login_followers_following)
map=[]
for _,row in login_followers_following.iterrows():
    map.append({"login":row['login'],"leader_strength":(row['followers']/(1+row['following']))})
    
x=pd.DataFrame(map)
x.sort_values(by='leader_strength',ascending=False,inplace=True)
print(x)
top_5=x[:5]
ans=''
for _,row in top_5.iterrows():
    ans+=row['login']+','

ans=ans[:-1]
print(ans)


    