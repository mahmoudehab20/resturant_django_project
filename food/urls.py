from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('main/<int:pk>',views.MainDetailView.as_view(),name="main"),
    path('appetizer/<int:pk>',views.AppetizersDetailView.as_view(),name="appetizers"),
    path('souce/<int:pk>',views.SouceDetailView.as_view(),name="souce"),
    path('addmain/',views.AddMainGenericView.as_view(),name="addmain"),
    path('addappe/',views.AddAppetizerGenericView.as_view(),name="addappe"),
    path('addsouce/',views.AddSouceGenericView.as_view(),name="addsouce"),
    path('maindel/<int:pk>',views.DeleteMainGenericView.as_view(),name="maindel"),
    path('appetizersdel/<int:pk>',views.DeleteAppetizersGenericView.as_view(),name="appedel"),
    path('soucedel/<int:pk>',views.DeletesouceGenericView.as_view(),name="soucedel"),
    path('buymain/<int:pk>',views.buymain,name="buymain"),
    path('buyappetizers/<int:pk>',views.buyappetizer,name="buyappe"),
    path('buysouce/<int:pk>',views.buysouce,name="buysouce"),
    path('editmain/<int:pk>',views.MainUpdateGenericView.as_view(),name="editmain"),
    path('editappe/<int:pk>',views.AppetizerUpdateGenericView.as_view(),name="editappe"),
    path('editsouce/<int:pk>',views.SouceUpdateGenericView.as_view(),name="editsouce"),
    path('signup/',views.registration.as_view(),name="signup"),
    
]