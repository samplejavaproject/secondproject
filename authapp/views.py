from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Create your views here.
def base_view(request):

    return render(request,'authapp/base.html')
@login_required()
def login_view(request):
    return render(request,'authapp/login.html')

def signup_view(request):
	form=SignUpForm()
	if request.method=="POST":
		form=SignUpForm(request.POST)
		user=form.save()
		user.set_password(user.password)
		user.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request,'authapp/signup.html',{'form':form})
