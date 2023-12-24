from django.urls import path , include

from . import views
urlpatterns = [

    path('',views.home ),
    path('get/',views.get_cooke ),
    path('del/',views.del_cookies ),

]