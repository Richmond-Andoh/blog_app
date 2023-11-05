from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Post

# Create your views here.



def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         email = request.POST['email']
#         password = request.POST['password']
#         password_confirm = request.POST['password_confirm']
        
#         if password == password_confirm:
#             if User.objects.filter(username = username).exists():
#                 messages.error(request, f'Username {username} already exists')
#                 return redirect('blog/register')
#             elif User.email.filter(email = email).exist():
#                 messages.error(request, f'Email {email} already exists')
#                 return redirect('blog/register')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()
#                 return redirect('blog/login')
            
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('blog/register')
        
#     else:
#         return render(request, 'blog/login.html')
    
         
#     return render(request, 'blog/register.html')


# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
        
#         user = auth.authenticate(email = email, password = password)
#         if user is not None:
#             auth.login(request, user)
#             redirect('blog/home')
            
#         else:
#             messages.error('Credentials are not captured in our database')
#             redirect('blog/login')
            
#     return render(request, 'blog/login.html')