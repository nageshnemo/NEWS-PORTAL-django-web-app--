from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'testapp/home.html')


def movie_news_view(request):
    news1 = "Due to election movie on biopic of india's primeminister(narendra modi) is postponed"
    news2 = "AVENGERS END GAME the last part of avengers serious is in cinemas"
    news3 = "BHARAT movie staring salman khan is coming on eid this year"
    my_dict = {'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/mnews.html',my_dict)


def sports_news_view(request):
    news1 = "dd"
    news2 = "dc"
    news3 = "csk"
    my_dict = {'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/snews.html',my_dict)



def politics_news_view(request):
    news1 = "modi"
    news2 = "modi"
    news3 = "modi"
    my_dict = {'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/pnews.html',my_dict)
