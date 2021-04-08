from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login_user(request):

    return render(request, 'login_user.html')


def register_user(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                print("the user is taken")
            elif User.objects.filter(email=email).exists():
                print("the email is taken")
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, password=password1, email=email)
                user.save()
                print("a user have been created")

        else:
            print('wrong password')

        return redirect('/')

    return render(request, 'register_user.html')


def user_profile(request):

    return render(request, 'profile.html')

# Create your views here.
