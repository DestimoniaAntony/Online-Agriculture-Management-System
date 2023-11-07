from django.shortcuts import redirect, render
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from agri_app.models import Booking, Crop, Farmer, Fertilizer,Researcher, Subsidy,User
class IndexView(TemplateView):
    template_name = "admin/index.html"
    
class PendingFarmerView(TemplateView):
    template_name = "admin/pending_Farmer_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(PendingFarmerView, self).get_context_data(**kwargs)

        farmer = Farmer.objects.filter(
            user__last_name='0', user__is_staff='0')
        
        context['farmer'] = farmer
        return context
    
class PendingResearcherView(TemplateView):
    template_name = "admin/pending_researcher_list.html"
    
    def get_context_data(self, **kwargs):
        context = super(PendingResearcherView, self).get_context_data(**kwargs)

        researcher = Researcher.objects.filter(
            user__last_name='0', user__is_staff='0')
        
        context['researcher'] = researcher
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/index.html', {'message': " Account Approved"})
    
class Reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        User.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'])
    
class CropRegView(TemplateView):
    template_name = 'admin/add_crops.html'      

    def post(self, request, *args, **kwargs):
        crop = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image) 
        amount = request.POST['amount'] 
        total_quantity = request.POST['quantity']
        
        obj = Crop()
        obj.crop = crop
        obj.description = description 
        obj.image = filesss  
        obj.amount = amount
        obj.total_quantity = total_quantity
        obj.save()
        
        return render(request, 'admin/index.html', {'message': "successfully added"})
    
class FertilizerRegView(TemplateView):
    template_name = 'admin/add_fertilizer.html'      

    def post(self, request, *args, **kwargs):
        fertilizer = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)  
        amount = request.POST['amount'] 
        total_quantity = request.POST['quantity']
        
        obj = Fertilizer()
        obj.fertilizer = fertilizer
        obj.description = description 
        obj.image = filesss  
        obj.amount = amount
        obj.total_quantity = total_quantity
        obj.save()
        
        return render(request, 'admin/index.html', {'message': "successfully added"})

class SubsidyRegView(TemplateView):
    template_name = 'admin/add_subsidies.html'      

    def post(self, request, *args, **kwargs):
        description = request.POST['description'] 
        
        obj = Subsidy()
        
        obj.description = description            
        obj.save()
        return render(request, 'admin/index.html', {'message': "successfully added"})
    
class ConfirmedBookingView(TemplateView):
    template_name = 'admin/booking.html'
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmedBookingView,self).get_context_data(**kwargs)
        view_booking = Booking.objects.filter(status='paid',payment='paid')

        context['view_booking'] = view_booking
        return context