from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from agri_app.models import Farmer, Researcher, UserType
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class FarmerRegView(TemplateView):
    template_name = 'farmer_reg.html'      

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'farmer_reg.html', {'message': "already added the username or email"})
        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()
            reg = Farmer()
            reg.user = user
            reg.age = age
            reg.mobile = mobile   
            reg.address = address    
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "farmer"
            usertype.save()

            return render(request, 'index.html', {'message': "successfully added"})
        
class ResearcherRegView(TemplateView):
    template_name = 'resercher_reg.html'      

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        qualification = request.POST['qualification']
        password = request.POST['password']
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'farmer_reg.html', {'message': "already added the username or email"})
        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()
            reg = Researcher()
            reg.user = user
            reg.qualification = qualification
            reg.mobile = mobile   

            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "researcher"
            usertype.save()

            return render(request, 'index.html', {'message': "successfully added"})
        
class loginview(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "farmer":
                    return redirect('/farmer')
                elif UserType.objects.get(user_id=user.id).type == "researcher":
                    return redirect('/researcher')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})