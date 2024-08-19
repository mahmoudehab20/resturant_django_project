from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import drinks
# Create your views here.

def drink_spec(request,itemID):
    drink=drinks.objects.get(pk=itemID)
    return render(request,'drinks/h4.html',{'drink':drink})

def add_drink(request):
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect('/food')
        drink=drinks(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
        drink.save()
        return HttpResponseRedirect('/food')
    return render(request,'drinks/adddrink.html')

def drinkdel(request,itemID):
    drink=drinks.objects.get(pk=itemID)
    drink.delete()
    return HttpResponseRedirect('/food')

def buydrink(request,itemID):
    drink=drinks.objects.get(pk=itemID)
    drink.stock-=1
    drink.save()
    return HttpResponseRedirect('/food')

def editdrinks(request,itemID):
    drink=drinks.objects.get(pk=itemID)
    if request.method=='POST':
        if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
            return HttpResponseRedirect('/food')
        drink.delete()
        drink=drinks(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
        drink.save()
        return HttpResponseRedirect('/food')
    return render(request,'drinks/editdrink.html',{'drink':drink})