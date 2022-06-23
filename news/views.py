import datetime

from django.shortcuts import render,HttpResponse,redirect
from info.models import news_table,comments,ads,news_letter


category=['Technology','Sports','Business','Entertainment']
def home(request):
    news = news_table.objects.all().order_by('-time')
    # category
    tech = news_table.objects.filter(category='Technology').reverse()
    sports = news_table.objects.filter(category='Sports').reverse()
    bus = news_table.objects.filter(category='Business').reverse()
    enter = news_table.objects.filter(category='Entertainment').reverse()
    cdt=datetime.datetime.now().strftime("%A, %B %m, %Y")
    ad=ads.objects.all().order_by('-date_from')

    if request.POST:
        eml = request.POST['eml']
        emlverfy = news_letter.objects.filter(email=str(eml))
        print(emlverfy)
        try:
            if eml != emlverfy[0].email:
                nl=news_letter(date_time=datetime.datetime.now(),email=eml)
                nl.save()
            else:
                return HttpResponse("already signup")
        except:
            nl = news_letter(date_time=datetime.datetime.now(), email=eml)
            nl.save()

    return render (request, "index.html",{"news":news,'cdt':cdt,'ad':ad,'tech':tech,'sports':sports,'bus':bus,'enter':enter})

def cat(request):
    ctg = news_table.objects.filter(category='Technology').reverse()
    return render(request,'category.html',{'ctg': ctg,'allcat':category})

def categ(request,cat):
    ctg = news_table.objects.filter(category=cat).reverse()

    if request.POST:
        eml = request.POST['eml']
        emlverfy = news_letter.objects.filter(email=str(eml))
        print(emlverfy)
        try:
            if eml != emlverfy[0].email:
                nl=news_letter(date_time=datetime.datetime.now(),email=eml)
                nl.save()
            else:
                return HttpResponse("already signup")
        except:
            nl = news_letter(date_time=datetime.datetime.now(), email=eml)
            nl.save()


    return render(request,'category.html',{'ctg':ctg,'allcat':category})

def contact(request):
    return render(request, 'contact.html')

def single(request,code):
    ne=news_table.objects.filter(id=code)
    com = comments.objects.filter(post_id=code)
    ncom = comments.objects.filter(post_id=code).count()+1

    if request.POST:
        post_id=code
        name = request.POST['name']
        email = request.POST['email']
        mob = request.POST['mob']
        comment = request.POST['comment']
        date_time = datetime.datetime.now()
        print(post_id,name,email,mob,comment,date_time)
        sc = comments(post_id_id=int(post_id),name=name,email=email,mob_no=mob,comment=comment,date_time=str(date_time))
        sc.save()

    return render(request,'single.html',{'ne':ne,'com':com,'ncom':ncom})


def login(request):
    if request.POST:
        uname = request.POST['uname']
        upsw = request.POST['psw']
        if uname == 'admin' and upsw == 'admin':
            return redirect('http://127.0.0.1:8000/showall/')

    return render(request,"login.html")

def showall(request):
    posts=news_table.objects.all()

    return render (request,'showall.html',{'posts':posts})


def delete(request,obj):
    news_table.objects.filter(id=obj).delete()

    posts = news_table.objects.all()
    return render (request,'showall.html',{'posts':posts})

def edit(request,id):
    data=news_table.objects.get(id=id)
    fil = news_table.objects.filter(id=id)
    print(data)
    if request.POST:
        cate = request.POST['category']
        title = request.POST['title']
        dec = request.POST['dec']
        youtube = request.POST['ytub']
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        try:
            image = request.FILES['img']
        except:
            image = fil[0].image
            print(image)
        print(image)
#Update
        data.title=title
        data.des=dec
        data.category = cate
        data.Pub_draft = True
        data.youtube_link = youtube
        data.date =date
        data.time = time
        data.image = image
        data.save()
        return showall(request)
        # blogpost = blog_table(title=title, des=dec, category=cate, pub_draft=True, youtube_link=youtube, date=date,time=time, image=image)
        # blogpost.save()

    return render (request,'post.html',{'data':fil,'cat':category})

def createPost(request):
    if request.POST:
        cate = request.POST['category']
        title = request.POST['title']
        dec = request.POST['dec']
        youtube = request.POST['ytub']
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
        time = today.strftime("%H:%M:%S")
        image = request.FILES['img']
        blogpost = news_table(title=title,des=dec,category=cate,youtube_link=youtube,date=date,time=time,image=image)
        blogpost.save()
        return redirect('http://127.0.0.1:8000/')

    return render(request, "post.html",{'cat':category})

