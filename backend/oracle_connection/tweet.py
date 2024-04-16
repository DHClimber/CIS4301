from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView

class API_tweet(APIView):
    def get(self, request, **kwargs):
        tweet_feed = """
        <!DOCTYPE html>
        <html>
        <body>
        <a class="twitter-timeline" href="https://twitter.com/TotalTrafficCHI?ref_src=twsrc%5Etfw" 
        height = "400" width = "400">Tweets by TotalTrafficCHI</a> <script async src="https://platform.twitter.com/widgets.js" 
        charset="utf-8"></script>
        </body>
        </html>

        """
        
        return HttpResponse(tweet_feed)