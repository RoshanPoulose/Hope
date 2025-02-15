"""
URL configuration for hopepro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hopeapp.views import index,contact,register,loginview,therapistregister
from hopeapp import admin_urls,user_urls,therapist_urls
from hopeapp import views




urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index.as_view()),
    path('contact',contact.as_view()),
    path('user_signup',register.as_view(),name='user_signup'),
    path('therapist_signup',therapistregister.as_view(),name='therapist_signup'),
    path('login/',loginview.as_view(),name='login'),
    path('user/',user_urls.urls()),
    path('admin/',admin_urls.urls()),
    path('therapist/',therapist_urls.urls()),
    # path('activate/<str:uidb64>/<str:token>/',views.activate_account, name='activate'),
    path("logout_user", views.logout_user, name='logout_user'),
    path("payment/<int:id>", views.payment, name='payment'),
    path("bookingview", views.bookingview, name='bookingview'),



]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

