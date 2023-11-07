from django.urls import path

from agri_app.farmer_views import FarmingTechniquesView, IndexView,CropView,FertilizerView, RejectcartView,SubsidyView,CartView,FertilizerCartView,BookingView,Payment, chpayment

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('cropview',CropView.as_view()),
    path('fertilizerview',FertilizerView.as_view()),
    path('subsidyview',SubsidyView.as_view()),
    path('addtocart',CartView.as_view()),
    path('adtocart',FertilizerCartView.as_view()),
    path('viewbooking',BookingView.as_view()),
    path('payment',Payment.as_view()),
    path('chpayment',chpayment.as_view()),
    path('remove',RejectcartView.as_view()),
    path('farmingtechniques',FarmingTechniquesView.as_view()),
]
def urls():
    return urlpatterns, 'farmer', 'farmer'