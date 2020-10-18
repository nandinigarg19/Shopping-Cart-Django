from django.shortcuts import render,HttpResponse
from . import helper as hp

def index(request):
    return render(request, 'shop/login.html')


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    params = {'msg':''}
    return render(request, 'shop/contact.html',params)

def addcontact(request):
    hp.saveCustomerFeedback()
    params = {'msg':'Query added successfully'}
    return render(request, 'shop/contact.html',params)
    
def tracker(request):
    return render(request, 'shop/about.html')

def cart(request):
    myProds = hp.getCartProducts(request)
    params = {'myProds': myProds}
    return render(request, 'shop/cart.html', params)

def login(request):
    params = {'msg': ''}
    return render(request, 'shop/login.html',params)

def userlogin(request):
    resp = hp.performLogin(request)
    if(resp == 0):
        params = {'msg': 'Invalid Login Credentials !!!'}
        return render(request, 'shop/login.html',params)  
    params = hp.getLoggedInParams("Login",request,resp['uname'])
    print(params)
    return render(request, 'shop/index.html',params)
    
def signup(request):
    params = hp.getSecurityDict()
    params['msg'] = ''
    return render(request, 'shop/signup.html', params)

def usersignup(request):
    resp = hp.saveUserInfo(request)
    if(resp == False):
        params = hp.getSecurityDict()
        params['msg'] = 'User with same email already exists !!!'
        return render(request, 'shop/signup.html', params)
    params = {'msg':'Sign up successful'}
    return render(request, 'shop/login.html', params)


        



        

