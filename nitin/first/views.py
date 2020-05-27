from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
	return render(request,'home.html')

def login(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		print('yes')
		if password1!=password2:
			messages.info(request,'passwords are not same')
			return redirect('login')
		elif User.objects.filter(username=username).exists():
			messages.info(request,'username already exists')
			return redirect('login')
		elif User.objects.filter(email=email).exists():
			messages.info(request,'email id is taken')
			return redirect('login')
		user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
		user.save();
		return redirect('register')
	else:
		return render(request,'login.html')



def register(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Not an authenticate user')
			return redirect('register')
	else:
		return render(request,'register.html')



def logout(request):
	auth.logout(request)
	return redirect('/')

# Create your views here.
