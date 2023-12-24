from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def home(request):
    responce = render(request,'home.html')
    # responce.set_cookie('name','Robi',max_age=10)
    responce.set_cookie('name','Robi',expires=datetime.utcnow()+timedelta(days=1))
    return responce

def get_cooke(request):
    name  = request.COOKIES.get('name')
    return render(request,'get.html',{'name':name})

def del_cookies(request):
    name = render(request,'del.html')
    name.delete_cookie('name')
    return name