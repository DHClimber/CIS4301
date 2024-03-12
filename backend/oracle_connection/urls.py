from django.urls import path

from oracle_connection.views import API_Connection, Dashboard

urlpatterns = [
    path("", API_Connection.as_view(), name="API for oracle from frontend"),
    path("dashboard/", Dashboard.as_view(), name="dashboard")
]