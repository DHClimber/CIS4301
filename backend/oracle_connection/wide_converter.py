import pandas as pd
import numpy as np

# df = Put the data into a dataframe first

# index should always be year, but columns will be a different variable each time. Same with values.
pivot = df.pivot_table(index="Year", columns="Street", values="Crashes")

json_arr = []

for i in range(len(pivot)):

    json_data = {}

    json_data["Year"] = pivot.index[i]

    for j in range(len(pivot.columns)):
        if not np.isnan(pivot.iloc[i, j]):
            json_data[pivot.columns[j]] = pivot.iloc[i, j]
    
    json_arr.append(json_data)

print(json_arr)
