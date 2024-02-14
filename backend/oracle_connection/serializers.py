from rest_framework import serializers

class ConnectionSerializer(serializers.Serializer):
    SQL_request = serializers.CharField(max_length=1000)

    
    