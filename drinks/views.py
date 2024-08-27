from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import drinks
from django.contrib import messages
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .forms import DrinksModelForm
# Create your views here.

# def drink_spec(request,itemID):
#     drink=drinks.objects.get(pk=itemID)
#     return render(request,'drinks/h4.html',{'drink':drink})

class DrinksDetailGenercView(DetailView):
    model=drinks
    template_name='drinks/h4.html'

# def add_drink(request):
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect('/food')
#         drink=drinks(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
#         drink.save()
#         return HttpResponseRedirect('/food')
#     return render(request,'drinks/adddrink.html')

class drinksCreateGenercView(CreateView):
    model=drinks
    form_class=DrinksModelForm
    template_name='drinks/adddrink.html'
    success_url='/food'

# def drinkdel(request,itemID):
#     drink=drinks.objects.get(pk=itemID)
#     drink.delete()
#     return HttpResponseRedirect('/food')

class DrinkDeleteGenercView(DeleteView):
    model=drinks
    template_name='drinks/drinkdel.html'

def buydrink(request,itemID):
    drink=drinks.objects.get(pk=itemID)
    if drink.stock!=0:
        drink.stock-=1
        drink.save()
        return HttpResponseRedirect('/food')
    else:
        messages.warning(request,'OUT OF STOCK!')
        return redirect('drink_spec')

# def editdrinks(request,itemID):
#     drink=drinks.objects.get(pk=itemID)
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect('/food')
#         drink.delete()
#         drink=drinks(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
#         drink.save()
#         return HttpResponseRedirect('/food')
#     return render(request,'drinks/editdrink.html',{'drink':drink})

class DrinkUpdateGenercView(UpdateView):
    model=drinks
    form_class=DrinksModelForm
    success_url='food'
    template_name='drinks/editdrink.html'
