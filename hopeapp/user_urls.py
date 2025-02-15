from django.urls import path
from hopeapp import user_views
from hopeapp.user_views import index,Profile,ViewAllDepressions,SingleDepressions,Search,SingleTherapists,Mysolutions,thankyou,UpdateProfile,booked_therapy,EnquiryForm
urlpatterns = [
    path('', index.as_view(),name='index'),
    path('ViewAllDepressions',ViewAllDepressions.as_view()),
    path('singlepageview',SingleDepressions.as_view()),
    path('myprofile',Profile.as_view()),
    path('search',Search.as_view(),name='search'),
    path('singletherapist',SingleTherapists.as_view(),name='singletherapist'),
    path('enquiries',Mysolutions.as_view()),
    # path('payment',userviews.payment,name='payment'),
    # path('chpayment',chpayment.as_view(),name='chpayment'),

    path('updateprofile',UpdateProfile.as_view()),
    path('thankyou',thankyou.as_view()),
    path('booked_therapy',booked_therapy.as_view()),
    path('EnquiryForm',EnquiryForm.as_view(),name='EnquiryForm')


]
def urls():
    return urlpatterns, 'user','user'