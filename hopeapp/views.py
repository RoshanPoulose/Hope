from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate, logout
from hopeapp.models import UserType, Registration, TherapistRegistration, BookedTherapists
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime, timedelta


# Create your views here.
class index(TemplateView):
    template_name = 'index.html'


class contact(TemplateView):
    template_name = 'contact.html'


class register(TemplateView):
    template_name = 'register.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')

            # user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
            #                                 is_staff=False, is_active=False)
            user.save()

            reg = Registration()  # call the model
            reg.user = user
            reg.name = name
            reg.email = email
            reg.phone = phone
            reg.location = location
            reg.password = password

            reg.save()

            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your account'
            # message = render_to_string('activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = email
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()

            # return render(request, 'verify_email.html', {'email': email})
            # messages="Registered Successfully"
            # return redirect('/')

            return render(request, 'index.html', {'message': "User Registered successfully"})


# def activate_account(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return render(request, 'index.html')  # Render a success message after activation
#     else:
#         return HttpResponse('Activation link is invalid or expired.')
class loginview(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                # if user.is_active == True:
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "therapist":
                    return redirect('/therapist')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})


class therapistregister(TemplateView):
    template_name = 'ther_register.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST['location']
        therapy_type = request.POST['type']
        about = request.POST['about']
        regnum = request.POST['regnum']
        fees = request.POST['fees']
        hname = request.POST['hname']
        pincode = request.POST['pincode']
        image = request.FILES['image']
        password = request.POST['password']
        ob = FileSystemStorage()
        obj = ob.save(image.name, image)

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html', {'message': "already added the username or email"})

        else:

            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            # user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
            #                                 is_staff=False, is_active=False)
            user.save()

            reg = TherapistRegistration()  # call the model
            reg.user = user
            reg.name = name
            reg.email = email
            reg.phone = phone
            reg.location = location
            reg.therapy_type = therapy_type
            reg.about = about
            reg.regnum = regnum
            reg.fees = fees
            reg.hname = hname
            reg.pincode = pincode
            reg.image = obj
            reg.password = password

            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "therapist"
            usertype.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your account'
            # message = render_to_string('activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # to_email = email
            # email = EmailMessage(mail_subject, message, to=[to_email])
            # email.send()

            # return render(request, 'verify_email.html', {'email': email})
            return render(request, 'index.html', {'message': "Therapist Registered successfully"})


def logout_user(request):
    logout(request)
    return redirect(reverse('login'))


def payment(request, id):
    us = Registration.objects.get(user_id=request.user.id)

    if BookedTherapists.objects.filter(therapy_id=id, user_id=us.id, status='Unlocked'):
        messages.success(request, "Already Unlocked This Therapist")

        return redirect('user:search')
    else:
        therapist = TherapistRegistration.objects.get(id=id)
        fee = therapist.fees
        tid = therapist.id
        print("ggrshh", id)
        return render(request, 'user/payment.html', {'fee': fee, 'tid': tid})

    # template_name="user/payment.html"


# def get_context_data(self, **kwargs):
#     context = super(payment, self).get_context_data(**kwargs)
#     id = self.request.GET['id']

#     if BookedTherapists.objects.filter(therapy_id=id,status='Unlocked'):
#         return render(self.request, 'user/search.html',{'message':"Already Unlocked "})
#     else:
#         therapist = TherapistRegistration.objects.get(id=id)
#         fee = therapist.fees
#             context['fee'] = fee
#         return context

#     def post(self, request, *args, **kwargs):
#         id=self.request.GET['id']
#         user = Registration.objects.get(user_id=request.user.id)

#         if BookedTherapists.objects.filter(therapy_id=id,status='Unlocked'):
#             return render(request, 'user/search.html',{'message':"Already Unlocked "})
#         else:
#             therapy_id = request.GET['id']
#             therapist = TherapistRegistration.objects.get(id=therapy_id)
#             fee = therapist.fees


#             us=Registration.objects.get(user_id=request.user.id)
#             abc=BookedTherapists()
#             abc.payment_date = datetime.now().date()
#             expiry_date = abc.payment_date + timedelta(days=15)
#             abc.expiry_date = expiry_date
#             abc.user_id=us.id
#             abc.therapy_id=id
#             abc.status='Unlocked'
#             abc.save()
#             return redirect('user:index')
def bookingview(request):
    us = Registration.objects.get(user_id=request.user.id)

    if request.method == 'POST':
        id = request.POST['id']
        abc = BookedTherapists()
        abc.payment_date = datetime.now().date()
        expiry_date = abc.payment_date + timedelta(days=15)
        abc.expiry_date = expiry_date
        abc.user_id = us.id
        abc.therapy_id = id
        abc.status = 'Unlocked'
        abc.save()
        return redirect('user:index')