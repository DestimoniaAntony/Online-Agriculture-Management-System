from django.urls import path

from agri_app.admin_views import IndexView,PendingFarmerView,PendingResearcherView,ApproveView,Reject,CropRegView,FertilizerRegView,SubsidyRegView,ConfirmedBookingView



urlpatterns = [
    
    path('',IndexView.as_view()),
    path('pending_farmer',PendingFarmerView.as_view()),
    path('pending_researcher',PendingResearcherView.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',Reject.as_view()),
    path('addcrop',CropRegView.as_view()),
    path('addfertilizer',FertilizerRegView.as_view()),
    path('addsubsidy',SubsidyRegView.as_view()),
    path('bookingview',ConfirmedBookingView.as_view()),
  
]
def urls():
    return urlpatterns, 'admin','admin'