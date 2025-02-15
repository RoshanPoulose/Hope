
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from hopeapp.models import Add_Category,Registration,TherapistRegistration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class index(LoginRequiredMixin,TemplateView):
    template_name='admin/index.html'
class category(LoginRequiredMixin,TemplateView):
    template_name='admin/add_category.html'

    def post(self, request, *args, **kwargs):
        category_name = request.POST['name']
        if Add_Category.objects.filter(category_name=category_name).exists():
            messages.warning(request, "The service '%s' is already added." %category_name)
            return render(request, 'admin/message.html')
        else:

            reg = Add_Category()
            reg.category_name = category_name
            reg.save()
            return redirect('admin:category')

class ViewCategory(LoginRequiredMixin,TemplateView):
    template_name='admin/view_category.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCategory, self).get_context_data(**kwargs)
        abc = Add_Category.objects.all()
        context = {
            'cate':abc
        }
        return context
class RemoveCategory(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Add_Category.objects.get(id=id).delete()
        return render(request, 'admin/index.html',{'message':"Category Removed "})

class view_therapist(LoginRequiredMixin,TemplateView):
    template_name='admin/view_therapist.html'
    def get_context_data(self, **kwargs):
        context = super(view_therapist, self).get_context_data(**kwargs)
        abc = TherapistRegistration.objects.all()
        context = {
            'therapists':abc
        }
        return context
class RemoveTherapist(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        User.objects.get(id=id).delete()
        return render(request, 'admin/index.html',{'message':"Successfully Removed Therapist"})
class view_users(LoginRequiredMixin,TemplateView):
    template_name='admin/view_users.html'
    def get_context_data(self, **kwargs):
        context = super(view_users, self).get_context_data(**kwargs)
        abc = Registration.objects.all()
        context = {
            'users':abc
        }
        return context
class RemoveUser(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Registration.objects.get(id=id).delete()
        return render(request, 'admin/index.html',{'message':"Successfully Removed"})
class Therapist_Verify(TemplateView):
    template_name='admin/approve_therapists.html'
    def get_context_data(self, **kwargs):
        context = super(Therapist_Verify,self).get_context_data(**kwargs)
        verify = TherapistRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['therapist'] = verify
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/index.html', {'message': " Account Approved"})