from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register( request ):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        
        if first_name == '':
            messages.info( request, 'Please enter your first name!')
            return redirect('register')
        
        elif email == '':
            messages.info( request, 'Please enter your email!')
            return redirect('register')
        
        elif password == '':
            messages.info( request, 'Please enter your password!')
            return redirect('register')
        
        elif confirm_password == '':
            messages.info( request, 'Please enter confirm password!')
            return redirect('register')
        
        elif username == '':
            messages.info( request, 'username not matching!')
            return redirect('register')
        
        elif password != confirm_password:
            messages.info( request, 'Password not matching!')
            return redirect('register')
        
        elif User.objects.filter( username=username ).exists() or User.objects.filter( email=email ).exists():
            messages.info( request, 'Username or Email already taken.' )
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save();
            messages.info( request, 'Successfully registered!')
            print("user created.")
            return redirect('login')
    else:
        return render(request, 'register.html')
    

def login( request ):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login( request, user)
            return redirect('/')
        else:
            messages.info( request, 'Invalid username or password!')
            return redirect('login')
    else:
        return render( request, 'login.html')
    
    
def logout( request ):
    auth.logout(request)
    return redirect('/')
