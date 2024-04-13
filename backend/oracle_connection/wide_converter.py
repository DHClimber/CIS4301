import pandas as pd
import numpy as np

# df = Put the data into a dataframe first

# index should always be year, but columns will be a different variable each time. Same with values.
def parse(data):
        
    keys = []
    for key in data['0']:
        keys.append(key)

    df = pd.DataFrame.from_dict(data).transpose()
   
    pivot = df.pivot_table(index=keys[0], columns=keys[1], values=keys[2])
    
    json_arr = []

    for i in range(len(pivot)):

        json_data = {}

        json_data["YEAR"] = pivot.index[i]

        for j in range(len(pivot.columns)):
            if not np.isnan(pivot.iloc[i, j]):
                json_data[pivot.columns[j]] = pivot.iloc[i, j]
        
        json_arr.append(json_data)

    #add index so it's easier to share across queries
    return_dict = {}
    index = 0
    for row in json_arr:
        return_dict[index] = row
        index += 1

    return return_dict

#for testing only
if __name__ == "__main__":
    parse({'0': {'YEAR': '2014', 'VEHICLE_TYPE': 'PASSENGER', 'INJURED_TO_CRASH': 0.25}, '1': {'YEAR': '2014', 'VEHICLE_TYPE': 'UNKNOWN/NA', 'INJURED_TO_CRASH': 0}, '2': {'YEAR': '2015', 'VEHICLE_TYPE': 'MOTOR DRIVEN CYCLE', 'INJURED_TO_CRASH': 0.67}, '3': {'YEAR': '2015', 'VEHICLE_TYPE': 'MOTORCYCLE (OVER 150CC)', 'INJURED_TO_CRASH': 0.35}, '4': {'YEAR': '2015', 'VEHICLE_TYPE': 'OTHER VEHICLE WITH TRAILER', 'INJURED_TO_CRASH': 0.13}, '5': {'YEAR': '2016', 'VEHICLE_TYPE': 'MOTORCYCLE (OVER 150CC)', 'INJURED_TO_CRASH': 0.43}, '6': {'YEAR': '2016', 'VEHICLE_TYPE': 'MOTOR DRIVEN CYCLE', 'INJURED_TO_CRASH': 0.33}, '7': {'YEAR': '2016', 'VEHICLE_TYPE': 'BUS OVER 15 PASS.', 'INJURED_TO_CRASH': 0.2}, '8': {'YEAR': '2017', 'VEHICLE_TYPE': 'MOTORCYCLE (OVER 150CC)', 'INJURED_TO_CRASH': 0.7}, '9': {'YEAR': '2017', 'VEHICLE_TYPE': 'MOTOR DRIVEN CYCLE', 'INJURED_TO_CRASH': 0.6}, '10': {'YEAR': '2017', 'VEHICLE_TYPE': 'FARM EQUIPMENT', 'INJURED_TO_CRASH': 0.5}, '11': {'YEAR': '2018', 'VEHICLE_TYPE': 'MOTORCYCLE (OVER 150CC)', 'INJURED_TO_CRASH': 0.72}, '12': {'YEAR': '2018', 'VEHICLE_TYPE': 'MOTOR DRIVEN CYCLE', 'INJURED_TO_CRASH': 0.66}, '13': {'YEAR': '2018', 'VEHICLE_TYPE': 'ALL-TERRAIN VEHICLE (ATV)', 'INJURED_TO_CRASH': 0.53}, '14': {'YEAR': '2019', 'VEHICLE_TYPE': 'MOTOR DRIVEN CYCLE', 'INJURED_TO_CRASH': 1}, '15': {'YEAR': '2019', 'VEHICLE_TYPE': 'BUS OVER 15 PASS.', 'INJURED_TO_CRASH': 0.38}, '16': {'YEAR': '2019', 'VEHICLE_TYPE': 'BUS UP TO 15 PASS.', 'INJURED_TO_CRASH': 0.25}})
