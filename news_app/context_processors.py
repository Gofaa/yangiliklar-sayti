# from news_app.models import News
#
# def latest_news(request):
#     latest_news = News.objects.all().order_by("-publish_time")[:10]
#     return {'latest_news': latest_news}