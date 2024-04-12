
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework import status
from oracle_connection.serializers import ConnectionSerializer
from rest_framework.views import APIView
from oracle_connection.oracle_interface import sql_request
from . import SQL

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
    
#Class view for getting all query results at once
class Dashboard(APIView):

    self.age_filter = "(age BETWEEN 0 AND 120 OR age IS NULL)"
    self.sex_filter = "(sex IN ('X', 'U', 'M', 'F') or sex IS NULL)"

    def post(self, request):
    
        CRASH_DATE_MIN = request.data['CRASH_DATE_MIN']
        if CRASH_DATE_MIN == "": CRASH_DATE_MIN = '01-01-2014'  

        CRASH_DATE_MAX = request.data['CRASH_DATE_MAX']
        if CRASH_DATE_MAX == "" : CRASH_DATE_MAX = '12-31-2019' 

        binder = [CRASH_DATE_MIN, CRASH_DATE_MAX, 'FOG/SMOKE/HAZE',
        'SEVERE CROSS WIND GATE', 'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
        'UNKNOWN', 'SLEET/HAIL']
        
        complex_sql1 = SQL.Query_1(self.age_filter, self.sex_filter) #working
        sql_response1 = sql_request(complex_sql1[0], binder)
        
        complex_sql2 = SQL.Query_2(self.age_filter, self.sex_filter) #working
        sql_response2 = sql_request(complex_sql2[0], binder)
       
        complex_sql3 = SQL.Query_3(self.age_filter, self.sex_filter) #working
        sql_response3 = sql_request(complex_sql3[0], binder)
       
        complex_sql4 = SQL.Query_4(self.age_filter, self.sex_filter) #working
        sql_response4 = sql_request(complex_sql4[0], binder)
            
        complex_sql5 = SQL.Query_5(self.age_filter, self.sex_filter) #working
        sql_response5 = sql_request(complex_sql5[0], binder)
        
        queryMap = {
            "1" : {
                "id" : "1",
                "title" : f"{complex_sql1[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql1[2]}",
                "data" : sql_response1.values()
                },
            "2" : {
                "id" : "2",
                "title" : f"{complex_sql2[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql2[2]}",
                "data" : sql_response2.values()
                },
            "3" : {
                "id" : "3",
                "title" : f"{complex_sql3[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql3[2]}",
                "data" : sql_response3.values()
            },
            "4" : {
                "id" : "4",
                "title" : f"{complex_sql4[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql4[2]}",
                "data" : sql_response4.values()
            },
            "5" : {
                "id" : "5",
                "title" : f"{complex_sql5[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql5[2]}",
                "data" : sql_response5.values()
            }
        }

        response_data =[queryMap["1"], queryMap["2"], queryMap["3"],queryMap["4"],queryMap["5"]]

  
        return Response(response_data)

    def get(self, request):

        binder = ['01-01-2014','12-31-2019', 'FOG/SMOKE/HAZE',
        'SEVERE CROSS WIND GATE', 'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
        'UNKNOWN', 'SLEET/HAIL']
        
        complex_sql1 = SQL.Query_1(self.age_filter, self.sex_filter) #working
        sql_response1 = sql_request(complex_sql1[0], binder)
        
        complex_sql2 = SQL.Query_2(self.age_filter, self.sex_filter) #working
        sql_response2 = sql_request(complex_sql2[0], binder)
       
        complex_sql3 = SQL.Query_3(self.age_filter, self.sex_filter) #working
        sql_response3 = sql_request(complex_sql3[0], binder)
       
        complex_sql4 = SQL.Query_4(self.age_filter, self.sex_filter) #working
        sql_response4 = sql_request(complex_sql4[0], binder)
            
        complex_sql5 = SQL.Query_5(self.age_filter, self.sex_filter) #working
        sql_response5 = sql_request(complex_sql5[0], binder)
        
        queryMap = {
            "1" : {
                "id" : "1",
                "title" : f"{complex_sql1[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql1[2]}",
                "data" : sql_response1.values()
                },
            "2" : {
                "id" : "2",
                "title" : f"{complex_sql2[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql2[2]}",
                "data" : sql_response2.values()
                },
            "3" : {
                "id" : "3",
                "title" : f"{complex_sql3[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql3[2]}",
                "data" : sql_response3.values()
            },
            "4" : {
                "id" : "4",
                "title" : f"{complex_sql4[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql4[2]}",
                "data" : sql_response4.values()
            },
            "5" : {
                "id" : "5",
                "title" : f"{complex_sql5[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql5[2]}",
                "data" : sql_response5.values()
            }
        }

        response_data =[queryMap["1"], queryMap["2"], queryMap["3"],queryMap["4"],queryMap["5"]]

  
        return Response(response_data)

#Class view for returning single SQL Queries 
#Format for passing K,V through url  /oracle_connection/dashboard_single/?view=1
#
# Format for POST request
# {"view": "1",
# "CRASH_DATE_MIN": "01-01-2014",
# "CRASH_DATE_MAX": "12-31-2019"
# }

class Dashboard_single(APIView):

    def post(self, request):
        
        view = request.data['view']

        if view == None:
            return Response({"error": 'please select 1-5 for key "view"'})

        sex = request.data['sex']
        min_age = request.data['min_age']
        max_age = request.data['max_age']
        weather = request.data['weather']

        CRASH_DATE_MIN = request.data['CRASH_DATE_MIN']
        if CRASH_DATE_MIN == "": CRASH_DATE_MIN = '01-01-2014'  

        CRASH_DATE_MAX = request.data['CRASH_DATE_MAX']
        if CRASH_DATE_MAX == "" : CRASH_DATE_MAX = '12-31-2019' 

        if weather == None: 
            weather = ['FOG/SMOKE/HAZE', 'SEVERE CROSS WIND GATE', 
                    'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
                    'UNKNOWN', 'SLEET/HAIL']

        binder = []

        binder.append(CRASH_DATE_MIN, CRASH_DATE_MAX)
        binder += weather
        binder += list(None for i in range(9 - len(weather)))

        age_filter = "age BETWEEN (:12) AND (:13)"

        binder += min_age
        binder += max_age
        
        if sex == "All":
            sex_filter = "(sex IN (:14, :15, :16, :17) or sex IS NULL)"
            binder += ['X', 'U', 'M', 'F']
        else:
            sex_filter = "sex IN (:14)"
            binder += sex

        #switch to retrieve requested sql request
        match view:
            case "1":
                complex_sql = SQL.Query_1(age_filter, sex_filter) #working
            case "2":
                complex_sql = SQL.Query_2(age_filter, sex_filter) #working
            case "3":
                complex_sql = SQL.Query_3(age_filter, sex_filter) #working
            case "4":
                complex_sql = SQL.Query_4(age_filter, sex_filter) #working
            case "5":
                complex_sql = SQL.Query_5(age_filter, sex_filter) #working
            
        sql_response = sql_request(complex_sql[0], binder)
        
        queryMap = {
                "id" : view,
                "title" : f"{complex_sql[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql[2]}",
                "data" : sql_response.values()
                }

        return Response(queryMap)
    
    def get(self, request):

        view = request.GET['view']

        age_filter = "(age BETWEEN 0 AND 120 OR age IS NULL)"
        sex_filter = "(sex IN ('X', 'U', 'M', 'F') or sex IS NULL)"
        
        binder = ['01-01-2014','12-31-2019', 'FOG/SMOKE/HAZE',
        'SEVERE CROSS WIND GATE', 'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
        'UNKNOWN', 'SLEET/HAIL']

        #switch to retrieve requested sql request
        match view:
            case "1":
                complex_sql = SQL.Query_1(age_filter, sex_filter) #working
            case "2":
                complex_sql = SQL.Query_2(age_filter, sex_filter) #working
            case "3":
                complex_sql = SQL.Query_3(age_filter, sex_filter) #working
            case "4":
                complex_sql = SQL.Query_4(age_filter, sex_filter) #working
            case "5":
                complex_sql = SQL.Query_5(age_filter, sex_filter) #working
            
        sql_response = sql_request(complex_sql[0], binder)
        
        queryMap = {
                "id" : view,
                "title" : f"{complex_sql[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql[2]}",
                "data" : sql_response.values()
                }

        return Response(queryMap)
    
#Query total tuples
class Schneider(APIView):

    def get(self, request):
        
        sql = """
            select count(*) AS "totalCount" FROM (SELECT RD_NO FROM CRASHES
            UNION ALL
            SELECT RD_NO FROM PEOPLE
            UNION ALL
            SELECT RD_NO FROM VEHICLES)
            """
        response = sql_request(sql,None)

        return Response(response.values())
