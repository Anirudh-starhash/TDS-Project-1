import pandas as pd
file=pd.read_csv("users.csv")

def update(x):
    if pd.isna(x) or x.strip()=='':
        return 0
    else:
        return len(x.split())

file['bio_length']=file['bio'].apply(update)

filtered_data = file[file['bio_length'] > 0]

x=pd.DataFrame(filtered_data['bio_length'])
y=pd.DataFrame(filtered_data['followers'])

from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()

lin_reg.fit(x,y)
slope=lin_reg.coef_[0][0]
print(round(slope,3))

