from django.shortcuts import render, redirect
from .forms import Userregisterform, Userupdateform, Profileupdateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Userregisterform(request.POST)
        if form.is_valid:
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Your account has been sucessfully created for { username }' )
                    return redirect('home')
    else:
        form = Userregisterform()                
    return render(request, 'users/register.html', { 'form' : form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = Userupdateform(request.POST,instance=request.user)
        p_form = Profileupdateform( request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been sucessfully updated' )
            return redirect('profile')
    else:
        u_form = Userupdateform(instance=request.user)
        p_form = Profileupdateform(instance=request.user.profile)


   
    context = {'u_form':u_form, 'p_form':p_form}

    return render(request, 'users/profile.html',context)    




    


