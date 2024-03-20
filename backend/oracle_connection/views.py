
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework import status
from oracle_connection.serializers import ConnectionSerializer
from rest_framework.views import APIView
from oracle_connection.oracle_interface import sql_request

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
            db_return = sql_request(sql_command)
            message = serializer.data
            message["db_response"] = str(db_return)
            return Response(message, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    
class Dashboard(APIView):

    def get(self, request):

        graphNum = request.GET.get("tile", None)

        if graphNum != None and graphNum not in ["1", "2", "3", "4", "5"]:
            return HttpResponseNotFound("Graph Number Not Found")
        
        crashes_by_year = sql_request("""SELECT EXTRACT(YEAR FROM CRASH_DATE) "name", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes GROUP BY EXTRACT(YEAR FROM CRASH_DATE) 
                                ORDER BY 1""")
        
        crashes_by_month = sql_request("""SELECT EXTRACT(MONTH FROM CRASH_DATE) "name", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes GROUP BY EXTRACT(MONTH FROM CRASH_DATE) 
                                ORDER BY 1""")
        
        crashes_by_day = sql_request("""SELECT CRASH_DAY_OF_WEEK "name", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes GROUP BY CRASH_DAY_OF_WEEK 
                                ORDER BY 1""")
        
        queryMap = {
            "1" : {
                "id" : "1",
                "title" : "Crashes per Year",
                "data" : crashes_by_year.values()
                },
            "2" : {
                "id" : "2",
                "title" : "Crashes per Month",
                "data" : crashes_by_month.values()
                },
            "3" : {
                "id" : "3",
                "title" : "Crashes per Day",
                "data" : crashes_by_day.values()
            }
        }

        if graphNum == None:
            response_data =[queryMap["1"], queryMap["2"], queryMap["3"]]

        else:
            response_data = queryMap[graphNum]


        return Response(response_data)
  