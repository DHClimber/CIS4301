import pandas as pd
import numpy as np
import oracledb

un = "Insert username here"
cs = "Insert host name here"
pw = "Insert password here"

def upload_crashes():

    ROW_NUMBER = 0

    crashes_df = pd.read_csv("datasets/crashes_cleaned.csv", index_col=0)

    crashes_df = crashes_df.replace(np.nan, None)
    
    crashes_df["INTERSECTION_RELATED_I"] = crashes_df["INTERSECTION_RELATED_I"].apply(lambda x: str(x).upper() if x != None else None)
    crashes_df["NOT_RIGHT_OF_WAY_I"] = crashes_df["NOT_RIGHT_OF_WAY_I"].apply(lambda x: str(x).upper() if x != None else None)
    crashes_df["HIT_AND_RUN_I"] = crashes_df["HIT_AND_RUN_I"].apply(lambda x: str(x).upper() if x != None else None)


    try:
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                for ROW_NUMBER in range(len(crashes_df)):

                    num_units = None
                    total_injuries = None
                    fatal_injuries = None
                    crash_hour = None
                    crash_day = None
                    crash_month = None

                    if crashes_df.iloc[ROW_NUMBER]["NUM_UNITS"] != None:
                        num_units = int(crashes_df.iloc[ROW_NUMBER]["NUM_UNITS"])
                    if crashes_df.iloc[ROW_NUMBER]["INJURIES_TOTAL"] != None:
                        total_injuries = int(crashes_df.iloc[ROW_NUMBER]["INJURIES_TOTAL"])
                    if crashes_df.iloc[ROW_NUMBER]["INJURIES_FATAL"] != None:
                        fatal_injuries = int(crashes_df.iloc[ROW_NUMBER]["INJURIES_FATAL"])
                    if crashes_df.iloc[ROW_NUMBER]["CRASH_HOUR"] != None:
                        crash_hour = int(crashes_df.iloc[ROW_NUMBER]["CRASH_HOUR"])
                    if crashes_df.iloc[ROW_NUMBER]["CRASH_DAY_OF_WEEK"] != None:
                        crash_day = int(crashes_df.iloc[ROW_NUMBER]["CRASH_DAY_OF_WEEK"])
                    if crashes_df.iloc[ROW_NUMBER]["CRASH_MONTH"] != None:
                        crash_month = int(crashes_df.iloc[ROW_NUMBER]["CRASH_MONTH"])

                    print(ROW_NUMBER, " row")
                    cursor.executemany("""INSERT INTO crashes VALUES(:1, TO_DATE(:2, 'mm/dd/YYYY'), :3, :4, :5, :6, :7, :8,
                    :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20,
                    :21, :22, :23, :24, :25, :26, :27)
                    """, [[crashes_df.iloc[ROW_NUMBER, 0], crashes_df.iloc[ROW_NUMBER, 1], int(crashes_df.iloc[ROW_NUMBER, 2]), crashes_df.iloc[ROW_NUMBER, 3], crashes_df.iloc[ROW_NUMBER, 4], 
                            crashes_df.iloc[ROW_NUMBER, 5], crashes_df.iloc[ROW_NUMBER, 6], crashes_df.iloc[ROW_NUMBER, 7], crashes_df.iloc[ROW_NUMBER, 8],
                            crashes_df.iloc[ROW_NUMBER, 9], crashes_df.iloc[ROW_NUMBER, 10], crashes_df.iloc[ROW_NUMBER, 11], crashes_df.iloc[ROW_NUMBER, 12], crashes_df.iloc[ROW_NUMBER, 13],
                            crashes_df.iloc[ROW_NUMBER, 14], crashes_df.iloc[ROW_NUMBER, 15], crashes_df.iloc[ROW_NUMBER, 16], crashes_df.iloc[ROW_NUMBER, 17], crashes_df.iloc[ROW_NUMBER, 18],
                            num_units, total_injuries, fatal_injuries, crash_hour, crash_day,
                            crash_month, crashes_df.iloc[ROW_NUMBER, 25], crashes_df.iloc[ROW_NUMBER, 26]]])
                    cursor.execute("COMMIT")
                    
                    
                    

    except Exception as e:
        print(e)
        print("THREW ERROR AT ROW ", ROW_NUMBER)
        print(crashes_df.iloc[ROW_NUMBER])

def upload_people():

    ROW_NUMBER = 0

    people_df = pd.read_csv("datasets/people_cleaned.csv", index_col=0)

    people_df = people_df.replace(np.nan, None)

    try:
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                for ROW_NUMBER in range(len(people_df)):

                    vehicle_id = None
                    age = None

                    if people_df.iloc[ROW_NUMBER]["VEHICLE_ID"] != None:
                        vehicle_id = int(people_df.iloc[ROW_NUMBER]["VEHICLE_ID"])
                    if people_df.iloc[ROW_NUMBER]["AGE"] != None:
                        age = int(people_df.iloc[ROW_NUMBER]["AGE"])

                    print(ROW_NUMBER, " row")
                    cursor.executemany("""INSERT INTO people VALUES(:1, :2, :3, :4, TO_DATE(:5, 'mm/dd/YYYY'), :6, :7, :8,
                    :9, :10, :11, :12, :13, :14, :15, :16)
                    """, [[people_df.iloc[ROW_NUMBER, 0], people_df.iloc[ROW_NUMBER, 1], people_df.iloc[ROW_NUMBER, 2], vehicle_id, people_df.iloc[ROW_NUMBER, 4], 
                            people_df.iloc[ROW_NUMBER, 5], people_df.iloc[ROW_NUMBER, 6], age, people_df.iloc[ROW_NUMBER, 8],
                            people_df.iloc[ROW_NUMBER, 9], people_df.iloc[ROW_NUMBER, 10], people_df.iloc[ROW_NUMBER, 11], people_df.iloc[ROW_NUMBER, 12], people_df.iloc[ROW_NUMBER, 13],
                            people_df.iloc[ROW_NUMBER, 14], people_df.iloc[ROW_NUMBER, 15]]])
                    cursor.execute("COMMIT")
                    
                    
                    

    except Exception as e:
        print(e)
        print("THREW ERROR AT ROW ", ROW_NUMBER)
        print(people_df.iloc[ROW_NUMBER])

def upload_vehicles():

    ROW_NUMBER = 0

    vehicles_df = pd.read_csv("datasets/vehicles_cleaned.csv", index_col=0)

    vehicles_df = vehicles_df.replace(np.nan, None)

    vehicles_df["EXCEED_SPEED_LIMIT_I"] = vehicles_df["EXCEED_SPEED_LIMIT_I"].apply(lambda x: str(x).upper() if x != None else None)

    try:
        with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
            with connection.cursor() as cursor:
                for ROW_NUMBER in range(len(vehicles_df)):

                    num_passengers = None
                    vehicle_id = None
                    occupant_count = None

                    if vehicles_df.iloc[ROW_NUMBER]["NUM_PASSENGERS"] != None:
                        num_passengers = int(vehicles_df.iloc[ROW_NUMBER]["NUM_PASSENGERS"])
                    if vehicles_df.iloc[ROW_NUMBER]["VEHICLE_ID"] != None:
                        vehicle_id = int(vehicles_df.iloc[ROW_NUMBER]["VEHICLE_ID"])
                    if vehicles_df.iloc[ROW_NUMBER]["OCCUPANT_CNT"] != None:
                        occupant_count = int(vehicles_df.iloc[ROW_NUMBER]["OCCUPANT_CNT"])

                    print(ROW_NUMBER, " row")
                    cursor.executemany("""INSERT INTO vehicles VALUES(:1, :2, TO_DATE(:3, 'mm/dd/YYYY'), :4, :5, :6, :7, :8,
                    :9, :10, :11, :12, :13, :14)
                    """, [[int(vehicles_df.iloc[ROW_NUMBER, 0]), vehicles_df.iloc[ROW_NUMBER, 1], vehicles_df.iloc[ROW_NUMBER, 2], int(vehicles_df.iloc[ROW_NUMBER, 3]), vehicles_df.iloc[ROW_NUMBER, 4], 
                            num_passengers, vehicle_id, vehicles_df.iloc[ROW_NUMBER, 7], vehicles_df.iloc[ROW_NUMBER, 8],
                            vehicles_df.iloc[ROW_NUMBER, 9], vehicles_df.iloc[ROW_NUMBER, 10], vehicles_df.iloc[ROW_NUMBER, 11], occupant_count, vehicles_df.iloc[ROW_NUMBER, 13]]])
                    cursor.execute("COMMIT")
                              

    except Exception as e:
        print(e)
        print("THREW ERROR AT ROW ", ROW_NUMBER)
        print(vehicles_df.iloc[ROW_NUMBER])

def main():
    
    upload_crashes()
    upload_people()
    upload_vehicles()
    



if __name__ == "__main__":
    main()