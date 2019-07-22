from django.views.generic import TemplateView
import MySQLdb
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib import auth 
from django.http import HttpResponseRedirect
from django.template import RequestContext
from pages.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from pages.forms import uploadform
from .filters import UserFilter
from pages.models import Post12,upload









def backg (request):
     
     if request.method=='POST':
           nik=AuthenticationForm
           aform =nik(data=request.POST or None)
           if aform.is_valid():
               return redirect('backg2')
             
     else:
          aform=AuthenticationForm()
     
     return render(request,'Home.html',{'aform':aform})
   
       

def archive (request):
    context ={}
    template = "archive.html"
    return render(request, template, context)

def backg1 (request):
    context ={}
    template = "About.html"
    return render(request, template, context)
    
def backg2 (request):
   if request.method=='POST':
        nik3=uploadform
        form=nik3(request.POST,request.FILES)
        
        if form.is_valid():
         
            form.save()
            return redirect('backg')
        else:
            return redirect('upload1.html')
   else:
    form=uploadform(request.POST,request.FILES)
    return render(request,'upload1.html',{'form':form})

def backg8 (request):
    context ={}
    template = "createpost.html"
    return render(request, template, context)


def newaccount(request):
      if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('upload1.html')
              
      else:
        form=AuthenticationForm()
        return render(request,'Home.html',{'form':form })
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post1()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, '1.html')  

        else:
                return render(request,'create.html')




def UserLogin(request):
      if request.method == 'POST':
        nik2=RegistrationForm
        form = nik2(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('backg')
      else:
        form = RegistrationForm()
      return render(request, 'signup.html', {'form': form})



    
         
def logout(request):
    
    return redirect('backg')

def search(request):
   from pages.models import Post12,Imageupload1
  

   error = False
   if 'q' in request.GET:
       q = request.GET['q']
       if not q:
          error = True
       else:
          data = upload.objects.filter(animaltype=q)
         
        
          return render(request, 'archive.html', {'data': data, 'query': q})
   return render(request, 'archive.html', {'error': error})




