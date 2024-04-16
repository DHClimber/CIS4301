#List of our complex queries that will be called by views.py

#1 Top Vehicle Types by Injury Rate in Crashes Involving Young Drivers
def Query_1(age_filter, sex_filter):
	sql = f"""
    SELECT Year,
        Vehicle_Type,
        Injured_to_Crash
    FROM (
        SELECT Year,
            Vehicle_Type,
            ROUND(SUM(Injured_Count) / COUNT(DISTINCT RD_NO), 2) AS Injured_to_Crash,
            RANK() OVER (
                PARTITION BY YEAR ORDER BY ROUND(SUM(Injured_Count) / COUNT(DISTINCT RD_NO), 2) DESC
                ) AS Rank
        FROM (
            SELECT TO_CHAR(C.CRASH_DATE, 'YYYY') AS Year,
                V.VEHICLE_TYPE AS Vehicle_Type,
                C.RD_NO,
                MAX(C.Injuries_Total) AS Injured_Count
            FROM Crashes C
            INNER JOIN People P ON C.RD_NO = P.RD_NO
            INNER JOIN Vehicles V ON P.VEHICLE_ID = V.VEHICLE_ID
            WHERE C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
                    AND TO_DATE(:2, 'MM-DD-YYYY')
	    AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
	    AND {age_filter} AND {sex_filter}
            GROUP BY TO_CHAR(C.CRASH_DATE, 'YYYY'),
                V.VEHICLE_TYPE,
                C.RD_NO
            )
        GROUP BY Year,
            Vehicle_Type
        ORDER BY Year,
            Injured_to_Crash DESC
        )
    WHERE Rank <= 3"""
	return [sql, "Top Vehicle Types by Injury to Crash Ratio","Injury Rate"]

#2 Top Contributory Causes of Traffic Crashes by Year
def Query_2(age_filter, sex_filter):
	sql = f"""
        SELECT Year,
        PRIM_CONTRIBUTORY_CAUSE,
        Total_Crashes
    FROM (
        SELECT TO_CHAR(c.CRASH_DATE, 'YYYY') AS Year,
            c.PRIM_CONTRIBUTORY_CAUSE,
            COUNT(DISTINCT(c.RD_NO)) AS Total_Crashes,
            DENSE_RANK() OVER (
                PARTITION BY TO_CHAR(c.CRASH_DATE, 'YYYY') ORDER BY COUNT(*) DESC
                ) AS Rank
        FROM Crashes c
        INNER JOIN people p
        ON p.RD_NO = c.RD_NO
        WHERE C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
                    AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY TO_CHAR(c.CRASH_DATE, 'YYYY'),
        PRIM_CONTRIBUTORY_CAUSE
        )
    WHERE Rank <= 5
    ORDER BY Year,
        Rank
    """
	return [sql, "Top Contributory Causes of Traffic Crashes by Year","Crash Count"]

#3 Annual Crash Counts on Top 5 Streets and Totals
def Query_3(age_filter, sex_filter):
	sql = f"""SELECT *
    FROM (
        SELECT EXTRACT(YEAR FROM c.CRASH_DATE) AS year,
            Street_Name,
            COUNT(DISTINCT(c.RD_NO)) as "Crash Count"
        FROM Crashes c
        INNER JOIN people p
        ON c.RD_NO = p.RD_NO
        WHERE Street_Name IN (
                SELECT Street_Name
                FROM crashes
                GROUP BY street_name
                ORDER BY COUNT(*) DESC FETCH FIRST 5 ROWS ONLY
                )
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
            AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM c.CRASH_DATE),
            Street_Name
        
        UNION
        
        SELECT EXTRACT(YEAR FROM c.CRASH_DATE) AS year,
            'Total',
            COUNT(DISTINCT(c.RD_NO)) as "Crash Count"
        FROM crashes c
        INNER JOIN people p
        ON p.RD_NO = c.RD_NO
        WHERE Street_Name IN (
                SELECT Street_Name
                FROM crashes
                GROUP BY street_name
                ORDER BY COUNT(*) DESC FETCH FIRST 5 ROWS ONLY
                )
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
            AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM c.CRASH_DATE)
        )
    ORDER BY YEAR ASC,
        3 ASC
	"""
	return [sql, "Annual Crash Counts on Top 5 (Overall) Streets and Totals","Crash Count"]

#4 Yearly Maximum Injuries by Vehicle Make
def Query_4(age_filter, sex_filter):
	sql = f"""
    WITH TEMP1
    AS (
        SELECT V.MAKE,
             C.RD_NO,
            Extract(YEAR FROM C.CRASH_DATE) AS YEAR,
            MAX(C.INJURIES_TOTAL) AS INJ
        FROM CRASHES C
        JOIN VEHICLES V ON C.RD_NO = V.RD_NO
		JOIN PEOPLE p ON C.RD_NO = p.RD_NO
		WHERE C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
            AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY Extract(YEAR FROM C.CRASH_DATE),
            V.MAKE,
            C.RD_NO
        ),
    TEMP2
    AS (
        SELECT TEMP1.MAKE,
            TEMP1."YEAR",
            SUM(TEMP1."INJ") AS INJ
        FROM TEMP1
        GROUP BY TEMP1.MAKE,
            TEMP1."YEAR"
        ),
    TEMP3
    AS (
        SELECT TEMP2.YEAR,
            MAX(TEMP2.INJ) AS INJ
        FROM TEMP2
        GROUP BY TEMP2.YEAR
        )
    SELECT TEMP2.YEAR,
        TEMP2.MAKE,
        TEMP2.INJ AS "Injury Count"
    FROM TEMP2,
        TEMP3
    WHERE TEMP2.YEAR = TEMP3.YEAR
        AND TEMP2.INJ = TEMP3.INJ
		AND TEMP2.YEAR <> 2014
    ORDER BY TEMP2.YEAR
    """
	return [sql, "Yearly Maximum Injuries by Vehicle Make", "Injury Count"]
	
#5 Comparative Analysis of Contributing Factors to Traffic Crashes by Year
def Query_5(age_filter, sex_filter):
	sql = f"""
    WITH Temp1
    AS (
        --Cell Phone
        SELECT EXTRACT(YEAR FROM C.CRASH_DATE) AS YEAR,
            ROUND(AVG(POSTED_LIMIT)) AS CELL_PHONE
        FROM Crashes C
		INNER JOIN People p
		ON p.RD_NO = c.RD_NO
        WHERE PRIM_CONTRIBUTORY_CAUSE IN (
                'CELL PHONE USE OTHER THAN TEXTING',
                'TEXTING'
                )
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
        AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM C.CRASH_DATE)
        ORDER BY 1 ASC
        ),
    Temp2
    AS (
        --DUI
        SELECT EXTRACT(YEAR FROM C.CRASH_DATE) AS YEAR,
            ROUND(AVG(POSTED_LIMIT)) AS DUI_CAUSE
        FROM Crashes C
		INNER JOIN People p
		ON p.RD_NO = c.RD_NO
        WHERE PRIM_CONTRIBUTORY_CAUSE IN ('UNDER THE INFLUENCE OF ALCOHOL/DRUGS (USE WHEN ARREST IS EFFECTED)')
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
        AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM C.CRASH_DATE)
	
        ),
    Temp3
    AS (
        --SPEED_LIMIT
        SELECT EXTRACT(YEAR FROM C.CRASH_DATE) AS YEAR,
            ROUND(AVG(POSTED_LIMIT)) AS EXCEEDED_SPEED_LIMIT
        FROM Crashes C
		INNER JOIN People p
		ON p.RD_NO = c.RD_NO
        WHERE PRIM_CONTRIBUTORY_CAUSE IN ('EXCEEDING AUTHORIZED SPEED LIMIT')
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
        AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM C.CRASH_DATE)
        ),
    Temp4
    AS (
        --NON_FATAL
        SELECT EXTRACT(YEAR FROM C.CRASH_DATE) AS YEAR,
            ROUND(AVG(POSTED_LIMIT)) AS NON_FATAL
        FROM Crashes C
		INNER JOIN People p
		ON p.RD_NO = c.RD_NO
        WHERE INJURIES_FATAL = 0
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
        AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM C.CRASH_DATE)
        ),
    Temp5
    AS (
        --FATAL
        SELECT EXTRACT(YEAR FROM C.CRASH_DATE) AS YEAR,
            ROUND(AVG(POSTED_LIMIT)) AS FATAL
        FROM Crashes C
		INNER JOIN People p
		ON p.RD_NO = c.RD_NO
        WHERE INJURIES_FATAL <> 0
		AND C.CRASH_DATE BETWEEN TO_DATE(:1, 'MM-DD-YYYY')
        AND TO_DATE(:2, 'MM-DD-YYYY')
        AND weather_condition IN (:3, :4, :5, :6, :7, :8, :9, :10, :11) 
        AND {age_filter} AND {sex_filter}
        GROUP BY EXTRACT(YEAR FROM C.CRASH_DATE)
        )
    SELECT Temp1.YEAR,
        Temp1.CELL_PHONE,
        Temp2.DUI_CAUSE,
        Temp3.EXCEEDED_SPEED_LIMIT,
        Temp4.NON_FATAL,
        Temp5.FATAL
    FROM Temp1,
        Temp2,
        Temp3,
        Temp4,
        Temp5
    WHERE Temp1.YEAR = Temp2.YEAR
        AND Temp2.YEAR = Temp3.YEAR
        AND Temp3.YEAR = Temp4.YEAR
        AND Temp4.YEAR = Temp5.YEAR
    ORDER BY Temp1.YEAR ASC
    """
	return [sql, "Comparative Analysis of Avg Speed Limit by Crash Type", "Speed Limit (mph)"]
