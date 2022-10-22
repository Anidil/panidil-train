import pandas as pd

organization = 'Anidil'
repository = 'panidil-train'
state = 'all'  # other options include 'closed' or 'open'

page = 1  # initialize page number to 1 (first page)
dfs = []  # create empty list to hold individual dataframes
# Note it is necessary to loop as each request retrieves maximum 30 entries
while True:
    url = f"https://api.github.com/repos/{repository}/pulls?" \
        f"state={state}&page={page}"
    dfi = pd.read_json(url)
    if dfi.empty:
        break
    dfs.append(dfi)  # add dataframe to list of dataframes
    page += 1  # Advance onto the next page

df = pd.concat(dfs, axis='rows', ignore_index=True)

# Create a new column with usernames
df['username'] = pd.json_normalize(df['user'])['login']