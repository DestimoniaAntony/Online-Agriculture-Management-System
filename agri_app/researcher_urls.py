from django.urls import path

from agri_app.researcher_views import IndexView,AddFarmingTechnique

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('addtechnique',AddFarmingTechnique.as_view()),
  
]
def urls():
    return urlpatterns, 'researcher', 'researcher'