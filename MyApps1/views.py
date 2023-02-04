from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
    request.session.set_test_cookie()
    print('cookies are getting set')
    return HttpResponse('<h1>Index page of cookies....</h1><hr/><h2>request check_view/url...</h2>')

def check_view(request):
   if request.session.test_cookie_worked():
        print('cookies are working now')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>cookie checking page working properly</h1>')
   else:
       print('cookies are not working')
       return HttpResponse('<h1>cookie checking page not working properly')

def count(request):
   if 'count' in request.COOKIES:
       newcount=int(request.COOKIES['count'])+1
   else:
       newcount=1

   response=render(request,'MyApps1.html',{'count':newcount})
   response.set_cookie('count',newcount)
   return response


from MyApps1.forms import LoginForm
import datetime
def home_view(request):
    formsobj=LoginForm()
    return render(request,'MyApps1/home.html',{'formsobj':formsobj})

def date_time_view(request):
    #form=LoginForm(request.GET)
    name=request.GET['name']
    response=render(request,'MyApps1/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response



def result_view(request):
    name=request.COOKIES['name']
    date_time=datetime.datetime.now()
    dict1={'name':name,'date_time':date_time}
    return render(request,'MyApps1/result.html',dict1)





def name_view(request):
    return render(request,'MyApps1/name.html')

def age_view(request):
    name=request.GET['name']
    response=render(request,'MyApps1/age.html',{'name':name})
    response.set_cookie('name',name,30)
    return response


def parent_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'MyApps1/parent.html',{'age':age,'name':name})
    response.set_cookie('age',age,30)
    return response

def result1(request):

    pname=request.GET['pname']
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    response=render(request,'MyApps1/result1.html',{'pname':pname,'name':name,'age':age})
    response.set_cookie('pname',pname,30)
    return response


from MyApps1.forms import ItemAddForm
def index1(request):
    return render(request,'MyApps1/home1.html')

def additem(request):
    formsobj=ItemAddForm()
    response=render(request,'MyApps1/additem.html',{'form1':formsobj})
    if request.method=='POST':
        formsobj=ItemAddForm(request.POST)
        if formsobj.is_valid():
            name=formsobj.cleaned_data['name']
            quantity=formsobj.cleaned_data['quantity']
            print(name,quantity)
            response.set_cookie(name,quantity,60)
    return response

def displayitem(request):
    return render(request,'MyApps1/showitems.html')

def page(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request,'MyApps1/count.html',{'count':newcount})

from MyApps1.forms import *

def name1(request):
    formsobj=NameForm()
    return render(request,'MyApps1/name1.html',{'form1':formsobj})

def age1(request):
    name=request.GET['name']
    request.session['name']=name
    formsobj2=AgeForm()
    return render(request,'MyApps1/age2.html',{'form2':formsobj2})

def pname2(request):

    age=request.GET['age']
    request.session['age']=age
    formsobj3=ParentForm()
    return render(request,'MyApps1/parent2.html',{'formsobj3':formsobj3})

def result2(request):
    pname=request.GET['pname']
    request.session['pname']=pname
    return render(request,'MyApps1/results2.html')

def additem(request):
    formsobj=AddItemForm()
    if request.method=='POST':
        #formsobj=AddItemForm(request.POST)
        #formsobj.cleaned_data['name']
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(30)

    return render(request,'MyApps1/additem1.html',{'formsobj':formsobj})

def dis(request):
    return render(request,'MyApps1/dis.html')