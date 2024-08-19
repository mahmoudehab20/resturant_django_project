from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MainDish,appetizers,souces
from drinks.models import drinks

def index(request):
    main=MainDish.objects.all()
    appe=appetizers.objects.all()
    souc=souces.objects.all()
    drink=drinks.objects.all()
    context={'main':main,'appetizers':appe,'souce':souc,'drink':drink}

    return render(request,'food/food.html',context)

def maindish_spec(request,itemID):
    main=MainDish.objects.get(pk=itemID)

    return render(request,'food/h1.html',{'main':main})

def appetizer_spec(request,itemID):
    appe=appetizers.objects.get(pk=itemID)
    
    return render(request,'food/h2.html',{'appetizers':appe})

def souce_spec(request,itemID):
    souce=souces.objects.get(pk=itemID)
    
    return render(request,'food/h3.html',{'souce':souce})

def add_maindish(request):
    if request.method == 'POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        main=MainDish(title=request.POST['title'],description=request.POST['description'],
                      price=request.POST['price'],stock=request.POST['stock'])
        main.save()
    
        return HttpResponseRedirect(reverse(index))
    
    return render(request,'food/addmain.html')

def add_appetizers(request):

    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        appe=appetizers(title=request.POST['title'],description=request.POST['description'],
                      price=request.POST['price'],stock=request.POST['stock'])
        appe.save()
    
        return HttpResponseRedirect(reverse(index))
    
    return render(request,'food/addappe.html')

def add_souce(request):
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        souce=souces(title=request.POST['title'],description=request.POST['description'],
            price=request.POST['price'],stock=request.POST['stock'])
        souce.save()
    
        return HttpResponseRedirect(reverse(index))
    
    return render(request,'food/addsouce.html')

def deletemain(request,itemID):
    main=MainDish.objects.get(pk=itemID)
    main.delete()
    return HttpResponseRedirect(reverse(index))

def deleteappe(request,itemID):
    appe=appetizers.objects.get(pk=itemID)
    appe.delete()
    return HttpResponseRedirect(reverse(index))

def deletesouce(request,itemID):
    souce=souces.objects.get(pk=itemID)
    souce.delete()
    return HttpResponseRedirect(reverse(index))

def buymain(request,itemID):
    main=MainDish.objects.get(pk=itemID)
    main.stock-=1
    main.save()

    return HttpResponseRedirect(reverse(index))

def buyappetizer(request,itemID):
    appe=appetizers.objects.get(pk=itemID)
    appe.stock-=1
    appe.save()
    
    return HttpResponseRedirect(reverse(index))

def buysouce(request,itemID):
    souce=souces.objects.get(pk=itemID)
    souce.stock-=1
    souce.save()
    
    return HttpResponseRedirect(reverse(index))

def editmain(request,itemID):
    main=MainDish.objects.get(pk=itemID)
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        main.delete()
        main=MainDish(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
        main.save()
        return HttpResponseRedirect(reverse(index))
    return render(request,'food/editmain.html',{'main':main})

def editappetizers(request,itemID):
    appe=appetizers.objects.get(pk=itemID)
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        appe.delete()
        appe=appetizers(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
        appe.save()
        return HttpResponseRedirect(reverse(index))
    return render(request,'food/editappe.html',{'appe':appe})

def editsouce(request,itemID):
    souce=souces.objects.get(pk=itemID)
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect(reverse(index))
        souce.delete()
        souce=souces(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
        souce.save()
        return HttpResponseRedirect(reverse(index))
    return render(request,'food/editsouce.html',{'souce':souce})