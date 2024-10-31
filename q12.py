import pandas as pd
file = pd.read_csv('users.csv')

hire = file[file['hireable'] == True]
unhire = file[file['hireable'] != True]

# Calculate the average 'following' for hireable and non-hireable users
avg_following_hireable = hire['following'].mean()
avg_following_non_hireable = unhire['following'].mean()

# Calculate the difference in averages
difference = avg_following_hireable - avg_following_non_hireable

# Print the difference rounded to 3 decimal places
print(round(difference, 3))
