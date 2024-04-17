
from rest_framework.response import Response
from rest_framework import status
from oracle_connection.serializers import ConnectionSerializer
from rest_framework.views import APIView
from oracle_connection.oracle_interface import sql_request
from . import SQL
from . import wide_converter as wc

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

    age_filter = "(age BETWEEN 0 AND 120 OR age IS NULL)"
    sex_filter = "(sex IN ('X', 'U', 'M', 'F') or sex IS NULL)"

    def post(self, request):
    
        if request.data['dates'][0] != "":
            CRASH_DATE_MIN = request.data['dates'][0]
        else:
            CRASH_DATE_MIN = '01-01-2014'  

        if request.data['dates'][1] != "":
            CRASH_DATE_MAX = request.data['dates'][1]
        else:
            CRASH_DATE_MAX = '12-31-2019'  

        binder = [CRASH_DATE_MIN, CRASH_DATE_MAX, 'FOG/SMOKE/HAZE',
        'SEVERE CROSS WIND GATE', 'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
        'UNKNOWN', 'SLEET/HAIL']

        #special binder for query 3
        binder_special3 = binder + binder

        #special binder for query 5
        binder_special5 = binder + binder + binder + binder + binder
        
        complex_sql1 = SQL.Query_1(self.age_filter, self.sex_filter) #working
        sql_response1 = wc.parse(sql_request(complex_sql1[0], binder))
               
        complex_sql2 = SQL.Query_2(self.age_filter, self.sex_filter) #working
        sql_response2 = wc.parse(sql_request(complex_sql2[0], binder))
       
        complex_sql3 = SQL.Query_3(self.age_filter, self.sex_filter) #working
        sql_response3 = wc.parse(sql_request(complex_sql3[0], binder_special3))
       
        complex_sql4 = SQL.Query_4(self.age_filter, self.sex_filter) #working
        sql_response4 = wc.parse(sql_request(complex_sql4[0], binder))
            
        complex_sql5 = SQL.Query_5(self.age_filter, self.sex_filter) #working
        sql_response5 = sql_request(complex_sql5[0], binder_special5)
        
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

        #because binding is positional, query 3 requires a list of 22 inputs for each position
        binder_special3 = binder + binder

        #special binder for query 5
        binder_special5 = binder + binder + binder + binder + binder
           
        complex_sql1 = SQL.Query_1(self.age_filter, self.sex_filter) #working
        sql_response1 = wc.parse(sql_request(complex_sql1[0], binder))
        
        complex_sql2 = SQL.Query_2(self.age_filter, self.sex_filter) #working
        sql_response2 = wc.parse(sql_request(complex_sql2[0], binder))
       
        complex_sql3 = SQL.Query_3(self.age_filter, self.sex_filter) #working
        sql_response3 = wc.parse(sql_request(complex_sql3[0], binder_special3))
        
        complex_sql4 = SQL.Query_4(self.age_filter, self.sex_filter) #working
        sql_response4 = wc.parse(sql_request(complex_sql4[0], binder))
            
        complex_sql5 = SQL.Query_5(self.age_filter, self.sex_filter) #working
        sql_response5 = sql_request(complex_sql5[0], binder_special5)

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
        
        #error catching when kv missing
        error_track = ""
        try:
            request.data['view']
        except Exception:
            error_track += "KV pair 'view' missing\n "
        try:
            request.data['sex']
        except Exception:
            error_track += "KV pair 'sex' missing\n "
        try:
            request.data['ageRange']
        except Exception:
            error_track += "KV pair 'ageRange' missing\n "
        try:
            request.data['weather']
        except Exception:
            error_track += "KV pair 'weather' missing\n "
        if error_track != "": return Response({"Error message": f"{error_track}"})
        
        view = str(request.data['view'])

        if view == None:
            return Response({"error": 'please select 1-5 for key "view"'})

        sex = request.data['sex']
        min_age = request.data['ageRange'][0]
        max_age = request.data['ageRange'][1]
        
        weather=[]
        if len(request.data['weather']) != 0:
            weather += request.data['weather']
        else:
            weather = ['FOG/SMOKE/HAZE', 'SEVERE CROSS WIND GATE', 
                'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
                'UNKNOWN', 'SLEET/HAIL']
            
        if request.data['dates'][0] != "":
            CRASH_DATE_MIN = request.data['dates'][0]
        else:
            CRASH_DATE_MIN = '01-01-2014'  

        if request.data['dates'][1] != "":
            CRASH_DATE_MAX = request.data['dates'][1]
        else:
            CRASH_DATE_MAX = '12-31-2019' 

        print(CRASH_DATE_MIN)
        print(CRASH_DATE_MAX)


        binder = []

        binder += [CRASH_DATE_MIN]
        binder += [CRASH_DATE_MAX]
        binder += weather
        binder += list(None for i in range(9 - len(weather)))

        if min_age == 0 and max_age == 120:
            age_filter = "(age BETWEEN (:12) AND (:13) OR age IS NULL)"
        else:
            age_filter = "age BETWEEN (:12) AND (:13)"


        binder += [min_age]
        binder += [max_age]
    
        if str.upper(sex) == "ALL":
            sex_filter = "(sex IN (:14, :15, :16, :17) or sex IS NULL)"
            binder += ['X', 'U', 'M', 'F']
        else:
            sex_filter = "sex IN (:14)"
            binder += [sex]

        if view == "3":
            binder += binder
        
        if view == "5":
            temp = []

            for i in range(5):
                for var in binder:
                    temp.append(var)
            binder = temp

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
        print(f"ERRRRR {sql_response}")
        print(f"Binder {binder}")
        print(f"Query {complex_sql[0]}")

        if int(view) < 5:
            sql_response = wc.parse(sql_response)
               
        queryMap = {
                "id" : view,
                "title" : f"{complex_sql[1]}",
                "xAxisLabel" : "year",
                "yAxisLabel" : f"{complex_sql[2]}",
                "data" : sql_response.values()
                }

        return Response(queryMap)
    
    def get(self, request):

        view = str(request.GET['view'])

        age_filter = "(age BETWEEN 0 AND 120 OR age IS NULL)"
        sex_filter = "(sex IN ('X', 'U', 'M', 'F') or sex IS NULL)"
        
        binder = ['01-01-2014','12-31-2019', 'FOG/SMOKE/HAZE',
        'SEVERE CROSS WIND GATE', 'SNOW', 'OTHER', 'CLEAR', 'RAIN', 'CLOUDY/OVERCAST',
        'UNKNOWN', 'SLEET/HAIL']

        if view == "3":
            binder += binder

        if view == "5":
            temp = []

            for i in range(5):
                for var in binder:
                    temp.append(var)
            binder = temp

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
        if int(view) < 5:
            sql_response = wc.parse(sql_response)

        print(f"Response {sql_response}")
        print(f"Binder {binder}")
        print(f"Query {complex_sql[0]}")

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
