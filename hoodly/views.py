from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewPostForm,NewProfileForm
from .models import Post,Profile
from django.contrib.auth.models import User
from .serializer import ProfileSerializer,PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
         form = UserCreationForm()
    return render (request,'registration/signup.html',{'form':form})

# @login_required(login_url='/accounts/login/')
def home(request):
    '''
    View for the main homepage.
    '''
    all_posts=Post.objects.all()
    logged_in_user = request.user
    logged_in_user_posts=Post.objects.filter(editor=logged_in_user)
    try:
        profile=Profile.objects.filter(editor=logged_in_user)
    except Profile.DoesNotExist:
        profile=None
    return render(request,'home.html',{"posts":logged_in_user_posts,"profile":profile,"allprojects":all_projects})    

class ProfileList(APIView):
    '''
    End point that returns all the profile details such as bio,
    profile_pic,projects posted and contact information
    '''
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)    

# @login_required(login_url='/accounts/login/')
def new_profile(request):
    '''
    Used for creating a new profile for the user. It includes a profile photo, a bio and contact 
    '''
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})  

# @login_required(login_url='/accounts/login/')
def single_post(request,post_id):
    '''
    This method displays a single photo and its details such as comments, date posted and caption
    '''

    post_posted=Post.single_post(post_id)  
    imageId=Post.get_image_id(post_id)
   

    

    return render(request,'post.html',{"post":post_posted})

class PostList(APIView):
    '''
    End point that returns all projects posted and the details such as title,
    image,description and live link to the project
    '''
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PosttSerializer(all_post, many=True)
        return Response(serializers.data)

#@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method == 'POST':
        uploadform = NewPostForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
       
            upload.save()
            return redirect('home_page')
    else:
        uploadform = NewPostForm()
    return render(request,'new_post.html',locals())   

# @login_required(login_url='/accounts/login/')
def display_profile(request,user_id):
    '''
    View for displaying a single profile
    '''
    try:
        single_profile=Profile.single_profile(user_id)              
        posts_posted=Post.user_posts(user_id)
        return render(request,'profiledisplay.html',{"profile":single_profile,"posts":posts_posted})
    except Profile.DoesNotExist:
        messages.info(request,'The user has not set a profile yet')
    except Post.DoesNotExist:
        messages.info(request,'The user has not posted a post yet')
        return redirect('home')        