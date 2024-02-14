from django.urls import path

from oracle_connection.views import API_Connection

urlpatterns = [
    path("", API_Connection.as_view(), name="API for oracle from frontend"),
]