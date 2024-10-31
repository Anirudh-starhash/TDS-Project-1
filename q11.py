

import pandas as pd
file=pd.read_csv("repositories.csv")

correlation = file['has_projects'].corr(file['has_wiki'])

# Print the result
print(round(correlation, 3))
