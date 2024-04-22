from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError,transaction
from accounts.models import KitchenOwner,Renter,Chife

# Create your views here.
def register_owner(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

        
            with transaction.atomic():
                
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                
                register_owner = KitchenOwner(user=new_user, commercial_register=request.FILES.get("commercial_register"),avatar=request.FILES.get("avatar", KitchenOwner.avatar.field.get_default()),phone=request.POST["phone"], verified=request.POST.get("verified",False))
                register_owner.save()

                
            return redirect("accounts:login_user")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_owner.html", {"msg" : msg})


def register_renter(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

        
            with transaction.atomic():
                
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                
                register_renter = Renter (user=new_user, about=request.POST["about"],avatar=request.FILES.get("avatar", KitchenOwner.avatar.field.get_default()),phone=request.POST["phone"])
                register_renter.save()

                
            return redirect("accounts:login_user")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_renter.html", {"msg" : msg})

def register_chife(request:HttpRequest):
    msg = None

    if request.method == "POST":
        try:

        
            with transaction.atomic():
                
                new_user = User.objects.create_user(username=request.POST["username"], email=request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
                new_user.save()

                
                register_chife= Chife(user=new_user,about=request.POST["about"] ,avatar=request.FILES.get("avatar", KitchenOwner.avatar.field.get_default()),phone=request.POST, cv=request.FILES.get("cv"))
                register_chife.save()

                
            return redirect("accounts:login_user")
        
        except IntegrityError as e:
            msg = "This username is already taken. Please choose a different username."
            print(e)

        except Exception as e:
            msg = "Something went wrong. Please try again."
            print(e)
    

    return render(request, "accounts/register_chife.html", {"msg" : msg})

def login_user(request:HttpRequest):
    msg = None

    if request.method == "POST":
    
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user:
            
            login(request, user)
            return redirect("main:home")
        else:
            msg = "Username or Password is wrong. Try again..."
    

    return render(request, "accounts/login_user.html", {"msg" : msg})

def logout_user(request:HttpRequest):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('accounts:login_user')