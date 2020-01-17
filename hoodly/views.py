from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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