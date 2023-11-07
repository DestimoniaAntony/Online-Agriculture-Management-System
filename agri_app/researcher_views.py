from django.shortcuts import render
from django.views.generic import TemplateView

from agri_app.models import FarmingTechnique

class IndexView(TemplateView):
    template_name = "researcher/index.html"
    
class AddFarmingTechnique(TemplateView):
    template_name = "researcher/add_farming_techniques.html"
    
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        description = request.POST['description'] 
        benefits = request.POST['benefits']
        
        abc = FarmingTechnique()
        
        abc.name = name 
        abc.description = description 
        abc.benefits = benefits            
        abc.save()
        
        return render(request, 'researcher/index.html', {'message': "successfully added"})