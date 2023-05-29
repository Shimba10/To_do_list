from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from templates import users,to_do_list_app
from to_do_list.settings import EMAIL_HOST_USER
from users.forms import RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
# Create your views here.
def signup(request):
    if request.method == 'GET':

        form = RegisterForm()
        return render(request, 'users/signup.html',{'form':form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form,'+++++++++++++++++++++++')
        name = request.POST['name']
        print(name,'========================')
        email = request.POST['email']
        print(email,'------------------------')
        if form.is_valid():
            form.save()
            send_mail(
                'Welcome to To-do_list family',
                'Hello ' +  name + ',' + 
                """ 
                
                
                Welcome to the To-do-list family.We're glad you're here.
                Here you will add what you want to do and after you've done the task, you can delete it in your time.
                If you want to edit, you can do that also. You have to create your profile and attach your profile pic. Later if you want to 
                update, you can update profile.
                Thank you for your time. If you have any questions just email me at shimba774@gmail.com
                
                Regards,
                Simanchal Polai""",
                EMAIL_HOST_USER,
                [email]
                

            )
            return redirect('../login/')
        else:
            return render(request, 'users/signup.html',{'form':form})
        
def login1(request):
    if request.method == 'GET':

        return render(request, 'users/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request,auth)
            return redirect('../home/')
        else:
            return render(request, 'users/login.html')
        