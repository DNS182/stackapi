from django.shortcuts import render
import requests
from .models import Questions
from django.db.models import Q


# Create your views here.

def index(request):
    datas = []
    if request.method == 'POST':
        search = request.POST['query']
        order = request.POST.get('order')
        sort = request.POST.get('sort')
        print(order ,sort)
        if search is not None :
            search_url = 'https://api.stackexchange.com/2.3/search/advanced'
            params ={
                    "order": order,
                    "sort" : sort,
                    "site" : "stackoverflow",
                    "title" : search,
                }
            r = requests.get(search_url , params=params)
            results = r.json()['items']
            for result in results:
                data = {
                    'title' : result['title'],
                    'link'  : result['link'],
                    'count' : result['answer_count'],
                    'answered' : result['is_answered'],
                    'view_count' : result['view_count'],
                    'asked_by' : result['owner']['link']
                }
                datas.append(data)
                value  = Questions.objects.create(title = data['title'], link = data['link'] , count = data['count'] , answered = data['answered'] , view_count = data['view_count'] , asked_by = data['asked_by'])
                value.save()

    # sending the page object to index.html
    return render(request , 'index.html' , { 'datas' : datas})


def cache(request ):
    datas = Questions.objects.all()
    context = {'datas' : datas}
    return render(request , 'cache.html', context)

def search(request):
    query = request.GET.get("query" , "")
    datas = Questions.objects.filter(Q(title__icontains = query))
    return render(request , 'search.html' , {'datas':datas , 'query':query})


