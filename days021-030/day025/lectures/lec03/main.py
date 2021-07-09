import pandas as pd

df = pd.read_csv("2018_squirrel_census.csv")

# My solution
new_df = df.groupby("Primary Fur Color", as_index=False).count()[['Primary Fur Color', 'X']]

columns = {
    'Primary Fur Color': 'Fur Color',
    'X': 'Count'
}
new_df.rename(columns=columns, inplace=True)

new_df.to_csv('squirrel_data.csv', index=False)

# Lecture solution
num_gray = len(df[df["Primary Fur Color"] == 'Gray'])
num_cinnamon = len(df[df["Primary Fur Color"] == 'Cinnamon'])
num_black = len(df[df["Primary Fur Color"] == 'Black'])

print(num_gray, num_cinnamon, num_black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_cinnamon, num_black]
}

new_df = pd.DataFrame(data_dict)
new_df.to_csv("squirrel_count.csv")
