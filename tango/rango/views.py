from django.shortcuts import render
from rango.forms import UserForm ,UserProfileForm,blogform
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import restrict
from django.shortcuts import render_to_response, get_object_or_404
def index(request):
 return render(request,'rango/index.html')
def register(request):

    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user
            profile.save()

            registered=True

        else :
            print (user_form.errors, profile_form.errors)

    else :
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,
            'rango/register.html',
            {'user_form':user_form , 'profile_form':profile_form, 'registered':registered}  )
def user_login(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(username=username,password=password)
  if user:
    if user.is_active:
     login(request,user)
     return render(request,'rango/index.html')
    else:
       return HttpResponse("your rango account is disabled")
  else:
       print ("invalid login details :{0},{1}".format(username,password))   
       return HttpResponse("invalid login details supplied")
 else:
    return render(request,'rango/login.html',{})
@login_required
def restricted(request):
    if request.method == 'POST':
        form = blogform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'rango/index.html')
        else:
            print (form.errors)
    else:
        form = blogform()
    return render(request, 'rango/restricted.html', {'form': form})
@login_required
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/rango/')
def search_form(request):
 return render(request,'rango/search_form.html')
def search(request):
 if 'q' in request.GET and request.GET['q']:
  q=request.GET['q']
  results = restrict.objects.filter(name__icontains=q)
  return render(request,'rango/search_results.html',{'results':results,'query':q})
 else:
   return HttpResponse('please submit a search term')
def view_post(request,slug):
 post = restrict.objects.get(slug=slug)
 post.views+=1
 post.save()
 return render(request,'rango/view_post.html',{'post':post})
