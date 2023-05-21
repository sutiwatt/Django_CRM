from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages




def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticated

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been log in')
            return redirect('home')
        else :
            messages.success(request,"There was Error")
            return redirect('home')
        
    else:
        return render(request,'home.html',{})
    

def logout_user(request):
    logout(request)
    messages.success(request,"You have been logout")
    return redirect('home')
