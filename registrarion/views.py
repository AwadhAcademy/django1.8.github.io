from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def registration(request):

    if request.method == 'POST':
        first_name=request.POST['first_name']
        phone=request.POST['phone']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        username=request.POST['user_name']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                # print('user name already exist')
                messages(request,'Username alredy taken')
            elif User.objects.filter(email=email).exists():
                print('email already exist')
            else:    
                user=User.objects.create_user(username=username,last_name=last_name,first_name=first_name,password=password1,email=email)
                user.save()
        else:
            print("password not match")
        return render(request,'confirm.html')
    else:
        return render(request,'login.html')

def confirm(request):
    return render(request,'confirm.html')

