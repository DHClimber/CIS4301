from django.urls import path

from oracle_connection.views import API_Connection, Dashboard, Schneider, Dashboard_single

urlpatterns = [
    path("", API_Connection.as_view(), name="API for oracle from frontend"),
    path("dashboard_single/", Dashboard_single.as_view(), name="dashboard_single"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("schneider/", Schneider.as_view(), name="show tuple count")
]