from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('',views.home,name='home'),
  path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('content/<str:id>',views.content,name="content"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.log_in,name="login"),
    path('logout/',views.log_out,name='logout')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


