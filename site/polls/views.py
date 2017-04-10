
# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'index.html',{'styles': 'polls/styles.css', 'title':"This is Ot first page"})
