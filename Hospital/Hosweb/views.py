from django.shortcuts import render,redirect
from Hosweb.models import Appointment
from django.contrib import messages

# Create your views here.

def home( request ):
    if request.method == 'POST':
        department = request.POST['department']
        doctor = request.POST['doctor']
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        email = request.POST['email']

        if department == '':
            messages.info( request, 'Please select a department!')
            return redirect('/')
        elif doctor == '':
            messages.info( request, 'Please select a doctor!')
            return redirect('/')
        elif date == '':
            messages.info( request, 'Please select a date!')
            return redirect('/')
        
        elif name == '':
            messages.info( request, 'Please enter your name!')
            return redirect('/')
        
        else:
            print('Appointment done!')
            app = Appointment(department=department ,doctor=doctor, name=name, date=date, time=time,email=email)
            app.save();
            messages.info( request, 'Appointment done!')
        return redirect('/')
    else:
        return render( request, 'index.html')

def about( request ):
    return render( request, 'about.html')

def price( request ):
    if request.method == 'POST':
        department = request.POST['department']
        doctor = request.POST['doctor']
        name = request.POST['name']
        date = request.POST['date']
        time = request.POST['time']
        email = request.POST['email']

        if department == '':
            messages.info( request, 'Please select a department!')
            return redirect('price')
        elif doctor == '':
            messages.info( request, 'Please select a doctor!')
            return redirect('price')
        elif date == '':
            messages.info( request, 'Please select a date!')
            return redirect('price')
        
        elif name == '':
            messages.info( request, 'Please enter your name!')
            return redirect('price')
        
        else:
            print('Appointment done!')
            app = Appointment(department=department ,doctor=doctor, name=name, date=date, time=time,email=email)
            app.save();
            messages.info( request, 'Appointment done!')
        return redirect('price')
    else:
        return render( request, 'price.html')