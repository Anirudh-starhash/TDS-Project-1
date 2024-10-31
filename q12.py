import pandas as pd
file=pd.read_csv("users.csv")

hire_count=len(file[file['hireable']==True])
unhire_count=len(file[file['hireable']!=True])

hfc=0
unhfc=0

for _,row in file.iterrows():
    if row['hireable']=='True':
        hfc+=row['following']
    else:
        unhfc+=row['following']
        
print(round((hfc/hire_count)-(unhfc/unhire_count),3))