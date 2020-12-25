from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method =='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}, Now Login to proceed !')
            return redirect('login')
    else :
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method =='POST':
        uuf=UserUpdateForm(request.POST,instance=request.user)
        puf=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if uuf.is_valid() and puf.is_valid():
            uuf.save()
            puf.save()
            messages.success(request,f'Your Account has been updated!')
            return redirect('profile')
    else :
        uuf = UserUpdateForm(instance=request.user)
        puf = ProfileUpdateForm(instance=request.user.profile)

    context={
        'uuf':uuf,
        'puf':puf
    }
    return render(request,'users/profile.html',context)