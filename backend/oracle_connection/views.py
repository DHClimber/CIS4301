
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework import status
from oracle_connection.serializers import ConnectionSerializer
from rest_framework.views import APIView
from oracle_connection.oracle_interface import sql_request

#Class for calling dynamic default values 
class Default():
    def min_date():
        sql = """SELECT min(Crash_Date) FROM Crashes"""
        response = str(sql_request(sql,None)['0']['MIN(CRASH_DATE)'])[:10]
        return response
    def max_date():
        sql = """SELECT max(Crash_Date) FROM Crashes"""
        response = str(sql_request(sql,None)['0']['MAX(CRASH_DATE)'])[:10]
        return response
    #gender default set based on most common occurence in data table
    def gender():
        sql = """SELECT (CASE WHEN Male - Female < 0 THEN 'F' ELSE 'M' END) AS SEX from (select count(sex) AS Female from people p1 where sex = 'F'), 
        (select count(sex) AS Male from people  p2 where sex = 'M')"""
        response = sql_request(sql,None)['0']['SEX']
        return response
    #This is not actual min, this is a range near the average age for default query
    def min_age():
        sql = """SELECT ROUND(AVG(Age) * 0.5,0) AS min_age FROM People"""
        response = str(sql_request(sql,None)['0']['MIN_AGE'])
        return response
    #This is not actual min, this is a range near the average age for default query
    def max_age():
        sql = """SELECT ROUND(AVG(Age) * 1.5,0) AS max_age FROM People"""
        response = str(sql_request(sql,None)['0']['MAX_AGE'])
        return response
    #default weather is set based on most common weather in table
    def weather():
        sql = """SELECT W1 AS Weather_condition FROM (SELECT W1  FROM (SELECT W1, C1 FROM (SELECT DISTINCT Weather_condition W1, count(Weather_condition) OVER(PARTITION BY Weather_condition)  AS C1 FROM CRASHES))
        CROSS JOIN 
        (SELECT W2, C2 FROM (SELECT DISTINCT Weather_condition W2, count(Weather_condition) OVER(PARTITION BY Weather_condition)  AS C2 FROM CRASHES))
        MINUS
        (SELECT W1 FROM (SELECT W1, C1 FROM (SELECT DISTINCT Weather_condition W1, count(Weather_condition) OVER(PARTITION BY Weather_condition)  AS C1 FROM CRASHES))
        CROSS JOIN 
        (SELECT W2, C2 FROM (SELECT DISTINCT Weather_condition W2, count(Weather_condition) OVER(PARTITION BY Weather_condition)  AS C2 FROM CRASHES))
        WHERE C1 < C2))"""
        response = str(sql_request(sql,None)['0']['WEATHER_CONDITION'])
        return response
    #default primary cause excludes unable to determine and selects the next most common primary cause
    def primary_cause():
        sql = """SELECT P1 AS Primary_cause FROM (SELECT P1  FROM (SELECT P1, C1 FROM (SELECT DISTINCT Prim_contributory_cause P1, count(Prim_contributory_cause) OVER(PARTITION BY Prim_contributory_cause)  AS C1 FROM CRASHES
        WHERE Prim_contributory_cause <> 'UNABLE TO DETERMINE'))
        CROSS JOIN 
        (SELECT P2, C2 FROM (SELECT DISTINCT Prim_contributory_cause P2, count(Prim_contributory_cause) OVER(PARTITION BY Prim_contributory_cause )  AS C2 FROM CRASHES
        WHERE Prim_contributory_cause <> 'UNABLE TO DETERMINE'))
        MINUS
        (SELECT P1 FROM (SELECT P1, C1 FROM (SELECT DISTINCT Prim_contributory_cause P1, count(Prim_contributory_cause) OVER(PARTITION BY Prim_contributory_cause)  AS C1 FROM CRASHES
        WHERE Prim_contributory_cause <> 'UNABLE TO DETERMINE'))
        CROSS JOIN 
        (SELECT P2, C2 FROM (SELECT DISTINCT Prim_contributory_cause P2, count(Prim_contributory_cause) OVER(PARTITION BY Prim_contributory_cause)  AS C2 FROM CRASHES
        WHERE Prim_contributory_cause <> 'UNABLE TO DETERMINE'))
        WHERE C1 < C2))"""
        response = str(sql_request(sql,None)['0']['PRIMARY_CAUSE'])
        return response

class API_Connection(APIView):
    
    #retrieve
    serializer_class = ConnectionSerializer

    def get(self, request, **kwargs):
        # #     #makes it possible to send get as URL type curl url/?keyword=value or GET HTTP with body

        # #     #checks if GET request has body
        if not bool(request.data):
            data = {"SQL_request": request.GET.get('SQL_request')}
        else:
            data = request.data

        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)

    # #create andor modify
    # #
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            sql_command = request.data["SQL_request"]
            db_return = sql_request(sql_command,None)
            message = serializer.data
            message["db_response"] = str(db_return)
            return Response(message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    
class Dashboard(APIView):

    def get(self, request):

        graphNum = request.GET.get("tile", None)
        min_date = request.GET.get("minDate", "")
        max_date = request.GET.get("maxDate", "")

        if graphNum != None and graphNum not in ["1", "2", "3", "4", "5"]:
            return HttpResponseNotFound("Graph Number Not Found")
        
        if min_date == "":
            min_date = "2000-01-01" # don't hardcode
        
        if max_date == "":
            max_date = "2025-01-01" # don't hardcode
        
        crashes_by_year = sql_request("""SELECT EXTRACT(YEAR FROM CRASH_DATE) "year", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes WHERE CRASH_DATE BETWEEN TO_DATE(:1, 'YYYY-MM-DD') 
                                AND TO_DATE(:2, 'YYYY-MM-DD') GROUP BY EXTRACT(YEAR FROM CRASH_DATE) 
                                ORDER BY 1""", [min_date, max_date])
        
        crashes_by_month = sql_request("""SELECT EXTRACT(MONTH FROM CRASH_DATE) "month", 
                                COUNT(*) "tuna" FROM 
                                Crashes WHERE CRASH_DATE BETWEEN TO_DATE(:1, 'YYYY-MM-DD') 
                                AND TO_DATE(:2, 'YYYY-MM-DD') GROUP BY EXTRACT(MONTH FROM CRASH_DATE) 
                                ORDER BY 1""", [min_date, max_date])
        
        crashes_by_day = sql_request("""SELECT CRASH_DAY_OF_WEEK "day", 
                                COUNT(*) "Number of Fatalities" FROM 
                                Crashes WHERE CRASH_DATE BETWEEN TO_DATE(:1, 'YYYY-MM-DD') 
                                AND TO_DATE(:2, 'YYYY-MM-DD') GROUP BY CRASH_DAY_OF_WEEK 
                                ORDER BY 1""", [min_date, max_date])
        
        queryMap = {
            "1" : {
                "id" : "1",
                "title" : "Crashes per Year",
                "xAxisLabel" : "year",
                "yAxisLabel" : "numCrashes",
                "data" : crashes_by_year.values()
                },
            "2" : {
                "id" : "2",
                "title" : "Crashes per Month",
                "xAxisLabel" : "month",
                "yAxisLabel" : "tuna",
                "data" : crashes_by_month.values()
                },
            "3" : {
                "id" : "3",
                "title" : "Crashes per Day",
                "xAxisLabel" : "day",
                "yAxisLabel" : "Number of Fatalities",
                "data" : crashes_by_day.values()
            }
        }

        if graphNum == None:
            response_data =[queryMap["1"], queryMap["2"], queryMap["3"]]

        else:
            response_data = queryMap[graphNum]


        return Response(response_data)

class Default_values(APIView):

    def get(self, request):
        response_data = {}
        response_data["min_date"] = Default.min_date()
        response_data["max_date"] = Default.max_date()
        response_data["gender"] = Default.gender()
        response_data["min_age"] = Default.min_age()
        response_data["max_age"] = Default.max_age()
        response_data["weather"] = Default.weather()
        response_data["primary cause"] = Default.primary_cause()
            
        return Response(response_data)