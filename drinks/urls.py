from django.urls import path 
from . import views
urlpatterns=[
    path('drink/<int:pk>',views.DrinksDetailGenercView.as_view(),name="drink"),
    path('adddrink/',views.drinksCreateGenercView.as_view(),name="adddrink"),
    path('drnkdel/<int:pk>',views.DrinkDeleteGenercView.as_view(),name="drinkdel"),
    path('buydrink/<int:pk>',views.buydrink,name="buydrink"),
    path('editdrink/<int:pk>',views.DrinkUpdateGenercView.as_view(),name="editdrink")
]