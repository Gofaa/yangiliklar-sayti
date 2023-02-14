from django.urls import path
from .views import news_list, news_detail, IndexView, ContactPageView, NoteFoundPage, LocalNewsView, TechnologyNewsView, ForeignNewsView, SportNewsView

urlpatterns = [
    path("", IndexView.as_view(), name='index_page'),
    path("news/", news_list, name="news_list"),
    path("news/<slug:news>/", news_detail, name="news_detail"),
    path("contact-us/", ContactPageView.as_view(), name="contact_page"),
    path("error-page/", NoteFoundPage, name="error_page"),
    path("local/", LocalNewsView.as_view(), name="local-news"),
    path("technology/", TechnologyNewsView.as_view(), name="technology-news"),
    path("foreign/", ForeignNewsView.as_view(), name="foreign-news"),
    path("sport/", SportNewsView.as_view(), name='sport-news'),
    ]