import traceback
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404

@login_required(login_url="/login/")
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        user = request.user

        Recipe.objects.create(
            # recipe_id=recipe_id,
            recipe_name=recipe_name,
            recipe_image= recipe_image,
            recipe_description= recipe_description,
            user=user
        )
        return redirect('/recipes/')
    queryset=Recipe.objects.filter(user=request.user)
    context={'recipes':queryset}

    return render(request,'recipe.html',context)


def delete_recipe(request,id):
  if request.method=='POST':
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')
  return HttpResponseForbidden("Invalid Request")

def update(request,id):
  queryset = get_object_or_404(Recipe, id=id)
  
#   if request.method=='POST':
#     return HttpResponseForbidden("You are not allowed to edit this Recipe")

  if request.method == 'POST':
    data = request.POST
    recipe_name=data.get('recipe_name')
    recipe_description=data.get('recipe_description')
    recipe_image=request.FILES.get('recipe_image')   

    queryset.recipe_name=recipe_name
    queryset.recipe_description=recipe_description

    if(recipe_image):
       queryset.recipe_image=recipe_image
    
    queryset.save()
    # return redirect('/recipes/')
  return render(request,'update_recipe.html',{'recipe':queryset})

def update_recipe(request, id):
    try:
        print("Entering update_recipe view")
        # queryset = get_object_or_404(Recipe, id=id)
        print(request.user)
        if Recipe.objects.filter(id=id, user=request.user).exists():
            queryset = Recipe.objects.get(id=id, user=request.user)
        else:
            raise Exception("Recipe Not Found")

        # if(queryset.user!=request.user):
        #     return HttpResponseForbidden("You are not allowed to edit this Recipe")
        # print("Rendering update_recipe.html")
        
        return render(request,'update_recipe.html',{'recipe':queryset})
    except Exception as e:
        print(traceback.format_exc())
        raise Exception(e)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/recipes/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login/')

    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request) 
    return redirect('/login/') 


   

def register_page(request):
    if request.method == 'POST':
    
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

      
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        
        messages.info(request, 'Account created successfully. Please log in.')
        return redirect('/login/')
    
    return render(request, 'register.html')

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def success_page(request):
    return render(request,'success_page.html')



def update_profile_photo(request):
    if request.method == 'POST' and request.FILES.get('profile_photo'):
        user_profile = request.user.profile
        user_profile.profile_photo = request.FILES['profile_photo']
        user_profile.save()
        return redirect('profile')  # Redirect back to the profile page

    return redirect('profile') 

