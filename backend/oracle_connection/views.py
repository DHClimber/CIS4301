
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
        crashes_by_year = sql_request("""SELECT EXTRACT(YEAR FROM CRASH_DATE) "year", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes GROUP BY EXTRACT(YEAR FROM CRASH_DATE) 
                                ORDER BY 1""")
        crashes_by_month = sql_request("""SELECT EXTRACT(MONTH FROM CRASH_DATE) "month", 
                                COUNT(*) "numCrashes" FROM 
                                Crashes GROUP BY EXTRACT(MONTH FROM CRASH_DATE) 
                                ORDER BY 1""")

        response_data = {
            "data1" : crashes_by_year.values(),
            "data2" : crashes_by_month.values()
        }

        return Response(response_data)
  