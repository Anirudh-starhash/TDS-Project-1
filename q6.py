import pandas as pd
file=pd.read_csv("users.csv")

file.sort_values(by=['created_at'],ascending=False,inplace=True)


joined_after_2020=[]
for x in file['created_at']:
    y=int(x[:4])
    if y>=2020:
        joined_after_2020.append(x)

users=[]
i=0
for x in file['login']:
    users.append(x)
    i+=1
    if i==len(joined_after_2020):
        break
    

file2=pd.read_csv("repositories.csv")
name_lan= file2[['login','language']]
map={}
for _,row in name_lan.iterrows():
    if row['login'] in users:
        if pd.isna(row['language']):
            continue
        
        if row['language'] not in map:
            map[row['language']]=0
        else:
            map[row['language']]+=1
            
max=-1
name=''

for x in map:
    if map[x]>max:
        max=map[x]
        name=x
        
second_max=-1
second_name=''

for x in map:
    if map[x]>second_max and map[x]<max:
        second_max=map[x]
        second_name=x
        
print(max,name)
print(second_max,second_name)


        