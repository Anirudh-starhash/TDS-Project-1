import pandas as pd
file2=pd.read_csv("repositories.csv")
lan_stars=file2[['language','stargazers_count']]
map={}
for _,row in lan_stars.iterrows():
    if row['language'] not in map:
        map[row['language']]={'count':1,'star':row['stargazers_count']}
    else:
        map[row['language']]['count']+=1
        map[row['language']]['star']+=row['stargazers_count']
        
max=-1
name=''
for x in map:
    if (map[x]['star']//map[x]['count'])>max:
        max=(map[x]['star']//map[x]['count'])
        name=x

print(name,max)