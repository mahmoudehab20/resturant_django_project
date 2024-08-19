from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('main/<int:itemID>',views.maindish_spec,name="main"),
    path('appetizer/<int:itemID>',views.appetizer_spec,name="appetizers"),
    path('souce/<int:itemID>',views.souce_spec,name="souce"),
    path('addmain/',views.add_maindish,name="addmain"),
    path('addappe/',views.add_appetizers,name="addappe"),
    path('addsouce/',views.add_souce,name="addsouce"),
    path('maindel/<int:itemID>',views.deletemain,name="maindel"),
    path('appetizersdel/<int:itemID>',views.deleteappe,name="appedel"),
    path('soucedel/<int:itemID>',views.deletesouce,name="soucedel"),
    path('buymain/<int:itemID>',views.buymain,name="buymain"),
    path('buyappetizers/<int:itemID>',views.buyappetizer,name="buyappe"),
    path('buysouce/<int:itemID>',views.buysouce,name="buysouce"),
    path('editmain/<int:itemID>',views.editmain,name="editmain"),
    path('editappe/<int:itemID>',views.editappetizers,name="editappe"),
    path('editsouce/<int:itemID>',views.editsouce,name="editsouce")
]