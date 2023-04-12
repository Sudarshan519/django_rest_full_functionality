from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings 
from users.models import CustomUser
from django.contrib.auth import authenticate,login,logout
def login_admin(request): 
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        if request.method=='GET':
            return render(request,'dashboard/login.html')
         
        elif request.method=='POST':
            username=(request.POST['username'])

            password=(request.POST['password'])
            user=authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:   
            return render(request,'dashboard/login.html')

from django.contrib.auth.decorators import login_required

@login_required(login_url='/dashboard/login/')
def dashboard(request):
    users=CustomUser.objects.all()
    return render(request,'dashboard/index.html',{"users":users})



def logout_view(request):
    logout(request)