from django.urls import path 
from . import views
urlpatterns=[
    path('drink/<int:itemID>',views.drink_spec,name="drink"),
    path('adddrink/',views.add_drink,name="adddrink"),
    path('drnkdel/<int:itemID>',views.drinkdel,name="drinkdel"),
    path('buydrink/<int:itemID>',views.buydrink,name="buydrink"),
    path('editdrink/<int:itemID>',views.editdrinks,name="editdrink")
]