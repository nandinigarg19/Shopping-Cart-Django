from .models import Product,Contact,User,UserLogin
from math import ceil
import pandas as pd
import json


def getAllProducts():
    allProds = []
    catProds = Product.objects.values('category','id')
    categories = sorted({item['category'] for item in catProds})
    for category in categories:
        prods = Product.objects.filter(category=category)
        n = len(prods)
        num_slides = (n//4 + ceil(n/4 - n//4))
        allProds.append([prods,num_slides,range(1,num_slides)])
    return allProds

def saveCustomerFeedback(request):
    if(request.method == 'POST'):
        cname = request.POST.get('cname','')
        cemail = request.POST.get('cemail','')
        cphone = request.POST.get('cphone','')
        cmsg = request.POST.get('cmsg','')
        crate = request.POST.get('crate',5)
        contact = Contact(contact_name=cname,contact_email=cemail,contact_phoneno=cphone,contact_msg=cmsg,contact_rate=crate)
        contact.save()

def getCartProducts(request):
    if(request.method == 'POST'):
        myProds = request.POST.get('itemsJson','')
        print(myProds)
        myProds = json.loads(myProds)
        for key in list(myProds.keys()):
            myProds[key]['price'] = int(myProds[key]['price'])
            myProds[key]['total'] = myProds[key]['price'] * myProds[key]['qty'] 
        print(type(myProds))
        print(myProds)
    return myProds
    
def isUserExist(email):
    k = list(UserLogin.objects.values('user_email'))
    k = [x['user_email'] for x in k]
    if(email in k):
        return True
    return False

def saveUserInfo(request):
    if(request.method == 'POST'):
        uemail = request.POST.get("user-email",'')
        if(isUserExist(uemail)):
            return False
        uname = request.POST.get("user-name",'')
        uphone = request.POST.get("user-phone",'')
        uadd1 = request.POST.get("user-add1",'')
        uadd2 = request.POST.get("user-add2",'')
        ucity = request.POST.get("user-city",'')
        ustate = request.POST.get("user-state",'')
        upincode = request.POST.get("user-pincode",'')
        upass = request.POST.get("user-pass",'')
        usq1 = request.POST.get("sq1",'')
        usq1ans = request.POST.get("user-sq1ans",'')
        usq2 = request.POST.get("sq2",'')
        usq2ans = request.POST.get("user-sq2ans",'')
        usq1 = getQuesFromSecurityDict(usq1)
        usq2 = getQuesFromSecurityDict(usq2)
    user = User(user_name=uname, user_phone=uphone, user_add1=uadd1, user_add2=uadd2,
                user_city=ucity, user_state=ustate, user_pincode=upincode,
                user_email=uemail, user_sq1=usq1, user_sq2=usq2,
                user_sq1ans=usq1ans, user_sq2ans=usq2ans)
    userlog = UserLogin(user_email=uemail, user_pass=upass)
    user.save()
    userlog.save()
    return True

def performLogin(request):
    if(request.method == 'POST'):
        ipemail = request.POST.get("inputEmail",'')
        if(not isUserExist(ipemail)):
            return 0
        upass = UserLogin.objects.filter(user_email=ipemail).values('user_pass')[0]['user_pass']
        ippass = request.POST.get("inputPassword",'')
        if(upass != ippass):
            return 0
    uname = User.objects.filter(user_email=ipemail).values('user_name')[0]['user_name']
    UserLogin.objects.filter(user_email=ipemail).update(user_loggedin=True)
    return {'uname':uname}
    
def getLoggedInParams(flag,request='',resp=''):
    params = {'allProds':getAllProducts()}
    if(request.method == 'POST'):
        if(flag=="Login"):
            params['uname'] = 'Hello, '+resp
        elif(flag== "Home"):
            kk = list(request.POST.keys())[1]
            params['uname'] = request.POST.get(kk)   
    else:
        params['uname'] = 'Login'
    return params






def getSecurityDict():
    sqdf = pd.read_csv('shop/static/shop/securityques.csv')
    sqdict1 = {}
    sqdict2 = {}
    n = len(sqdf)
    for i in range(0,n//2):
        sqdict1[sqdf.loc[i,'qno']] = sqdf.loc[i,'ques']
    for i in range(n//2,n):
        sqdict2[sqdf.loc[i,'qno']] = sqdf.loc[i,'ques']
    return {'sqdict1':sqdict1,'sqdict2':sqdict2}

def getQuesFromSecurityDict(qno):
    sqdict = getSecurityDict()
    print(sqdict)
    if(qno in sqdict['sqdict1'].keys()):
        return sqdict['sqdict1'][qno]
    elif(qno in sqdict['sqdict2'].keys()):
        return sqdict['sqdict2'][qno]

