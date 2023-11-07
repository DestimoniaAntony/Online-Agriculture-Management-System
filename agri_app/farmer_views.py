from typing import Any, Dict
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View

from agri_app.models import Booking, Crop, Farmer, FarmingTechnique, Fertilizer, Subsidy

class IndexView(TemplateView):
    template_name = "farmer/index.html"
    
class CropView(TemplateView):
    template_name = "farmer/crop_view.html"
    
    def get_context_data(self, **kwargs):
        context = super(CropView, self).get_context_data(**kwargs)
        view_pp = Crop.objects.all()
        context['view_pp'] = view_pp
        return context   

class FertilizerView(TemplateView):
    template_name = "farmer/fertilizer_view.html"
    
    def get_context_data(self, **kwargs):
        context = super(FertilizerView, self).get_context_data(**kwargs)
        view_fertilizer = Fertilizer.objects.all()
        context['view_fertilizer'] = view_fertilizer
        return context
    
class SubsidyView(TemplateView):
    template_name = "farmer/subsidy_view.html"
    
    def get_context_data(self, **kwargs):
        context = super(SubsidyView, self).get_context_data(**kwargs)
        view_subsidy = Subsidy.objects.all()
        context['view_subsidy'] = view_subsidy
        return context
    
class CartView(View):
    def dispatch(self,request,*args,**kwargs):
        id = self.request.POST['id']
        qty = request.POST['qty']
        crop = Crop.objects.get(pk=id)        
        amount=crop.amount
        crop.total_quantity=int(crop.total_quantity)-int(qty)
        crop.save()
        ca = Booking()
        
        re = Farmer.objects.get(user_id=self.request.user.id)
        
        ca.crop_id=id        
        ca.amount=amount
        ca.quantity=qty
        ca.user_id=re.id
        ca.payment = 'null'
        ca.status = 'selected'
        ca.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})

class FertilizerCartView(View):
    def dispatch(self,request,*args,**kwargs):
        id = self.request.POST['id']
        qty = request.POST['qty']
        fertilizer = Fertilizer.objects.get(pk=id) 
        fertilizer.total_quantity=int(fertilizer.total_quantity)-int(qty)
        fertilizer.save()       
        amount=fertilizer.amount
        
        ca = Booking()
        
        re = Farmer.objects.get(user_id=self.request.user.id)
       
        ca.fertilizer_id=id        
        ca.amount=amount
        ca.quantity=qty
        ca.user_id=re.id
        ca.payment = 'null'
        ca.status = 'selected'
        ca.save()
        return redirect(request.META['HTTP_REFERER'],{'message':"Item selected"})
    
class BookingView(TemplateView):
    template_name = 'farmer/selected_package.html'
    def get_context_data(self, **kwargs):
        context = super(BookingView, self).get_context_data(**kwargs)
        user = Farmer.objects.get(user_id=self.request.user.id)
        ct = Booking.objects.filter(status='selected',user_id=user.id)
        total = 0   
        for i in ct:
            total = total + int(i.amount) * int(i.quantity)

        context['view_cart'] = ct
        context['asz'] = total

        return context

class Payment(TemplateView):
    template_name = 'farmer/payment.html'
    def get_context_data(self, **kwargs):
        context = super(Payment, self).get_context_data(**kwargs)
        user = Farmer.objects.get(user_id=self.request.user.id)
        ct = Booking.objects.filter(status='selected',user_id=user.id)
        total = 0   
        for i in ct:
            total = total + (int(i.amount)) * int(i.quantity)

        context['view_cart'] = ct
        context['asz'] = total

        return context
    
class chpayment(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        farmer = Farmer.objects.get(user_id=self.request.user.id)
        ch = Booking.objects.filter(user_id=farmer.id,status='selected')
        print(ch)
        for i in ch:
            i.payment = 'paid'
            i.status = 'paid'
            i.save()
        return render(request,'farmer/index.html',{'message':" payment Success"})
    
class RejectcartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Booking.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"cart"})

class FarmingTechniquesView(TemplateView):
    template_name = "farmer/view_farming_techniques.html"
    
    def get_context_data(self, **kwargs):
        context = super(FarmingTechniquesView, self).get_context_data(**kwargs)
        view_ft = FarmingTechnique.objects.all()
        context['view_ft'] = view_ft
        return context