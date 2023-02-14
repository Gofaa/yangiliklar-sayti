from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

#from django.views.generic import  TemplateView
from .models import News,  Category
from .forms import ContactForm

"""
#class HomePageView(TemplateView):
#    template_name = 'news/index.html'

class news_list(ListView):
    model = News
    template_name = 'news/news_list.html'
    #context_object_name = "news_list"


class news_detail(DetailView):
    model = News
    template_name = 'news/news_detail.html'

#class IndexView(request):
#    news = News.objects.filter(status = News.Status.Published)
#    categories

"""
def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published) # Published bo'lganlarni publish qiladi
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)


# def IndexView(request):
#     categories = Category.objects.all()
#     news_list = News.objects.all().order_by('-publish_time')[:6]
#     first_local_news = News.objects.all().filter(category__name='Maxalliy').order_by("-publish_time")[:1]
#     local_news = News.objects.all().filter(category__name='Maxalliy').order_by("-publish_time")[1:6]
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_news': local_news,
#         'first_local_news': first_local_news,
#     }
#
#     return render(request, "news/index.html", context)

class IndexView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.objects.all().order_by('-publish_time')[:6]
        context['local_news'] = News.objects.all().filter(category__name='Maxalliy').order_by("-publish_time")[:5]
        context['foreign_news'] = News.objects.all().filter(category__name='Xorij').order_by("-publish_time")[:5]
        context['technology_news'] = News.objects.all().filter(category__name='Texnalogiya').order_by("-publish_time")[:5]
        context['sport_news'] = News.objects.all().filter(category__name='Sport').order_by("-publish_time")[:5]
        return context

# def ContactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse(" Biz bilan bog'langaningiz uchun raxmat")
#     context = {
#         "form": form
#     }

#    return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = "news/contact.html"

    def get(self,request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self,request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur </h2>")
        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)




def NoteFoundPage(request):
    context = {

    }

    return  render(request, 'news/404.html', context)


class LocalNewsView(ListView):
    model = News
    template_name = "news/mahalliy.html"
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published,  category__name="Maxalliy")
        return news

class ForeignNewsView(ListView):
    model = News
    template_name = "news/xorij.html"
    context_object_name = 'xorijiy-yangiliklar'
    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published,  category__name="Xorij")
        return news

class SportNewsView(ListView):
    model = News
    template_name = "news/sport.html"
    context_object_name = 'sport-yangiliklar'
    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published,  category__name="Sport")
        return news

class TechnologyNewsView(ListView):
    model = News
    template_name = "news/texnalogiya.html"
    context_object_name = 'texnalogiya-yangiliklar'
    def get_queryset(self):
        news = self.model.objects.filter(status=News.Status.Published,  category__name="Texnalogiya")
        return news



