from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings 
from users.models import CustomUser
def login(request): 
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        username=(request.POST['username'])

        password=(request.POST['password'])
        # user=authenticate()
        if user is not None:
            return redircet('dashboard')
        return render(request,'dashboard/login.html')

from django.contrib.auth.decorators import login_required

@login_required(login_url='/dashboard/login/')
def dashboard(request):
    users=CustomUser.objects.all()
    return render(request,'dashboard/index.html',{"users":users})