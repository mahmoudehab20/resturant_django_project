from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MainDish,appetizers,souces
from drinks.models import drinks
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from django.contrib import messages
from .forms import MainModelForm,AppetizersModelForm,SouceModelForm

class registration(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = 'acc/login'

def index(request):
    main=MainDish.objects.all()
    appe=appetizers.objects.all()
    souc=souces.objects.all()
    drink=drinks.objects.all()
    context={'main':main,'appetizers':appe,'souce':souc,'drink':drink}

    return render(request,'food/food.html',context)

# def maindish_spec(request,itemID):
#     main=MainDish.objects.get(pk=itemID)

#     return render(request,'food/h1.html',{'main':main})

class MainDetailView(DetailView):
    model=MainDish
    template_name='food/h1.html'
    context_object_name='main'


# def appetizer_spec(request,itemID):
#     appe=appetizers.objects.get(pk=itemID)
    
#     return render(request,'food/h2.html',{'appetizers':appe})

class AppetizersDetailView(DetailView):
    model=appetizers
    template_name='food/h2.html'

# def souce_spec(request,itemID):
#     souce=souces.objects.get(pk=itemID)
    
#     return render(request,'food/h3.html',{'souce':souce})

class SouceDetailView(DetailView):
    model=souces
    template_name='food/h3.html'
    context_object_name='souce'

# def add_maindish(request):
#     if request.method == 'POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         main=MainDish(title=request.POST['title'],description=request.POST['description'],
#                       price=request.POST['price'],stock=request.POST['stock'])
#         main.save()
    
#         return HttpResponseRedirect(reverse(index))
    
#     return render(request,'food/addmain.html')

class AddMainGenericView(CreateView):
    form_class=MainModelForm
    template_name='food/addmain.html'
    success_url='/food'

# def add_appetizers(request):

#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         appe=appetizers(title=request.POST['title'],description=request.POST['description'],
#                       price=request.POST['price'],stock=request.POST['stock'])
#         appe.save()
    
#         return HttpResponseRedirect(reverse(index))
    
#     return render(request,'food/addappe.html')

class AddAppetizerGenericView(CreateView):
    form_class=AppetizersModelForm
    template_name='food/addappe.html'
    success_url='/food'

# def add_souce(request):
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         souce=souces(title=request.POST['title'],description=request.POST['description'],
#             price=request.POST['price'],stock=request.POST['stock'])
#         souce.save()
    
#         return HttpResponseRedirect(reverse(index))
    
#     return render(request,'food/addsouce.html')

class AddSouceGenericView(CreateView):
    form_class=SouceModelForm
    template_name='food/addsouce.html'
    success_url='/food'

# def deletemain(request,itemID):
#     main=MainDish.objects.get(pk=itemID)
#     main.delete()
#     return HttpResponseRedirect(reverse(index))

class DeleteMainGenericView(DeleteView):
    model=MainDish
    template_name='food/maindel.html'
    success_url='/food'
    context_object_name='main'

# def deleteappe(request,itemID):
#     appe=appetizers.objects.get(pk=itemID)
#     appe.delete()
#     return HttpResponseRedirect(reverse(index))

class DeleteAppetizersGenericView(DeleteView):
    model=appetizers
    template_name='food/appedel.html'
    success_url='/food'
    context_object_name='appe'

# def deletesouce(request,itemID):
#     souce=souces.objects.get(pk=itemID)
#     souce.delete()
#     return HttpResponseRedirect(reverse(index))

class DeletesouceGenericView(DeleteView):
    model=souces
    template_name='food/soucedel.html'
    success_url='/food'
    context_object_name='souce'

def buymain(request,itemID):
    main=MainDish.objects.get(pk=itemID)
    if main.stock!=0:
        main.stock-=1
        main.save()
    else:
        messages.warning(request,'OUT OF STOCK!')
        return redirect('maindish_spec')
    return HttpResponseRedirect(reverse(index))
    
def buyappetizer(request,itemID):
    appe=appetizers.objects.get(pk=itemID)
    if appe.stock!=0:
        appe.stock-=1
        appe.save()
    else:
        messages.warning(request,'OUT OF STOCK!')
        return redirect('appetizer_spec')
    return HttpResponseRedirect(reverse(index))

def buysouce(request,itemID):
    souce=souces.objects.get(pk=itemID)
    if souce.stock!=0:
        souce.stock-=1
        souce.save()
    else:
        messages.warning(request,'OUT OF STOCK!')
        return redirect('souce_spec')
    return HttpResponseRedirect(reverse(index))

# def editmain(request,itemID):
#     main=MainDish.objects.get(pk=itemID)
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         main.delete()
#         main=MainDish(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
#         main.save()
#         return HttpResponseRedirect(reverse(index))
#     return render(request,'food/editmain.html',{'main':main})

class MainUpdateGenericView(UpdateView):
    model=MainDish
    form_class=MainModelForm
    template_name='food/editmain.html'
    success_url='/food'

# def editappetizers(request,itemID):
#     appe=appetizers.objects.get(pk=itemID)
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         appe.delete()
#         appe=appetizers(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
#         appe.save()
#         return HttpResponseRedirect(reverse(index))
#     return render(request,'food/editappe.html',{'appe':appe})

class AppetizerUpdateGenericView(UpdateView):
    model=appetizers
    form_class=AppetizersModelForm
    template_name='food/editappe.html'
    success_url='/food'

# def editsouce(request,itemID):
#     souce=souces.objects.get(pk=itemID)
#     if request.method=='POST':
#         if request.POST['title']=='' or request.POST['description']=='' or request.POST['price']=='' or request.POST['stock']=='':
#             return HttpResponseRedirect(reverse(index))
#         souce.delete()
#         souce=souces(title=request.POST['title'],description=request.POST['description'],price=request.POST['price'],stock=request.POST['stock'])
#         souce.save()
#         return HttpResponseRedirect(reverse(index))
#     return render(request,'food/editsouce.html',{'souce':souce})

class SouceUpdateGenericView(UpdateView):
    model=souces
    form_class=SouceModelForm
    template_name='food/editsouce.html'
    success_url='/food'
