from django.shortcuts import render,redirect
from . forms import LoginForm,SignForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import User
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request,'index.html')



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session['user_id'] = user.id
                    last_login = request.user.last_login
                    last_login_str = timezone.localtime(last_login).strftime('%Y-%m-%d %H:%M:%S')
                    context = {'last_login': last_login_str}
                    return render(request,'dashboard.html',context)
                else:
                    messages.info(request, 'User is not Active',extra_tags='danger')
            else:
                user_obj = User.objects.filter(username=username).first()
                if user_obj is None:
                    messages.error(request, 'Username not found',extra_tags='danger')
                else:
                    messages.error(request, 'Wrong Password',extra_tags='danger')
        else:
            messages.warning(request, 'Check your username or Password')
    else:
        form = LoginForm()
    return render(request,'login.html', {'form':form})


def user_signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Account has been created. Now you can Log in!')
            return redirect('login')
    else:
        form = SignForm()
    return render(request, 'signup.html',{'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = User
    return render(request, 'dashboard.html')
    

def user_logout(request):
    logout(request)
    request.session.pop('user_id', None)
    return redirect('index')


