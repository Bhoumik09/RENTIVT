from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import Contact,Upload
from django.contrib import messages
import random
# password for test user is Harry$$$***000
# Create your views here.



from django.db.utils import IntegrityError

def registerUser(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        Rpassword = request.POST.get("create_password")
        if(password=="" or Rpassword==""):
            messages.error(request,"Password field cannot be empty")
            return redirect('/register')
        if(len(str(password))<8):
            messages.error(request,"Password should be of lenth 8 and above")
            return redirect('/register')
        if(" " in str(username)):
            messages.error(request,"There should not be any spaces in the username")
            return redirect('/register')
        # Check if a user with the same username already exists
        if password==Rpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken. Please choose a different username.")
                return redirect('/register')
            
            try:
                # Attempt to create the new user
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, "User registered successfully.")
                return redirect('/login')
            except IntegrityError:
                messages.error(request, "Error occurred while registering the user.")
                return redirect('/register')
       
            

    
    return render(request, "register.html")


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        message=request.POST.get("message")
        if message:  # Check if 'message' is not empty
            contact = Contact(name=name, email=email, phone=phone, message=message)
            
            try:
                contact.save()
                messages.success(request, "Feedback has been successfully sent")
            except IntegrityError:
                messages.error(request, "Error occurred while saving the feedback.")
        else:
            messages.error(request, "Message field is required 1.")
        
        # messages.success(request, "Feedback has been successfully sent")
    return render(request,"index.html")
   
def upload(request):

    # photo = request.FILES['photo']

    if request.method=="POST":
        # id=random.randrange(1,100000000000000
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        photo = request.POST.get("photo")
        inUse=request.POST.get("inUse")
        type1=request.POST.get("type1")
        description=request.POST.get("description")
        if(type1) :
            uploads=Upload(id=random.randrange(1,1000000000000000),name=name,email=email,phone=phone,photo=photo,inUse=inUse,type1=type1,description=description)
            try:
                uploads.save()
                messages.success(request, "Item Uploaded Succesfully")
            except IntegrityError:
                messages.error(request, "Error occurred while uploading the Item")
        else:
            messages.error(request, "Message field is required.")
        # uploads.save()
        # messages.success(request, "Your Item has been uploaded.Our team will verify and list the item soon")
    return render(request,"upload.html")



def loginUser(request):
    # count=0
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request,"Welcome "+str(user))

            return redirect("/")

        else:
           
            messages.error(request,"The Username or password entered is Incorrect")
            return redirect("/login")
            

            # No backend authenticated the credentials
            

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
def cycles(request):
     return render(request, 'cycles.html')
def books(request):
     return render(request, 'books.html')
def matress(request):
     return render(request, 'matress.html')
def lamps(request):
     return render(request, 'lamps.html')
