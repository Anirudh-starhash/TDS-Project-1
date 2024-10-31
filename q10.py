import pandas as pd
file=pd.read_csv("users.csv")
from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
x=pd.DataFrame(file["followers"])
y=pd.DataFrame(file["public_repos"])
lin_reg.fit(y,x)

# Output the regression slope (coefficient)
slope = lin_reg.coef_[0][0]  # Access the first (and only) element
print(f"Regression slope of followers on repos: {slope:.3f}")