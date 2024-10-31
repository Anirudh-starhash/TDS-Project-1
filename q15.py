import pandas as pd
file=pd.read_csv('users.csv')

hire_count=len(file.loc[file['hireable']==True])
unhire_count=len(file['hireable'])-hire_count
total=hire_count+unhire_count

def get_count(x):
    e=0
    for _,row in x.iterrows():
        if pd.isna(row['email']) or row['email'].strip()=='':
            pass
        else:
            e+=1
        
    return e
        

hire=pd.DataFrame(file.loc[file['hireable']==True])
unhire=pd.DataFrame(file.loc[file['hireable']!=True])


ehc=get_count(hire)

uehc=get_count(unhire)

print(round((ehc/hire_count)-(uehc/unhire_count),3))

