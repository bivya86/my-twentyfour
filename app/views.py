from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')
    return render(request,'insert_topic.html')
def insert_Webpage(request):
    QST=Topic.objects.all()
    d={'topic':QST}
    if request.method=="POST":
        tn=request.POST.get('topic')
        n=request.POST['name']
        u=request.POST['url']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T,name=n,url=u)[0]
        W.save()
        
        return HttpResponse('insert_Webpage is created')
    return render(request,'insert_Webpage.html',d)

def insert_Accessrecords(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    if request.method=="POST":
        Wp=request.POST['name']
        d=request.POST['date']
        W=Webpage.objects.get_or_create(name=Wp)[0]
        W.save()
        A=Accessrecords.objects.get_or_create(name=W,date=d)[0]
        A.save()
        return HttpResponse('insert_Accessrecords is created')
    return render(request,'insert_Accessrecords.html',d)


def select_multiple(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    if request.method=='POST':
        tos=request.post.getlist('topics')
        W=Webpage.objects.none()
        for i in tos:
            W=W|Webpage.objects.filter(topic_name=i)
        d1={'Webpage':W}
    
        return render(request,'insert_Webpage.html',d1)

    return render(request,'select_multiple.html',d)

def checkbox(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'checkbox.html',d)