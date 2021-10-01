from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import SignUpForm,EditForm
from django.views.generic import DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework.views import APIView
from .serializers import ListDetailSerailizer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.status import HTTP_401_UNAUTHORIZED
import requests
import datetime
# Create your views here.
class ListDetail(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=CustomUser.objects.filter(is_staff=False)
        serializer = ListDetailSerailizer(user,many=True)
        return Response({'result':serializer.data})


def auth_register(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        forms = SignUpForm()
        if request.method == 'POST':
            forms = SignUpForm(request.POST)
            print ('Register')
            if forms.is_valid():
                forms.save()
                return redirect('userapp:auth-login')
    return render(request, 'userapp/register.html',{'forms': forms,})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
                email = request.POST.get('email')
                password = request.POST.get('password')
                user=authenticate(request,username=email,password=password)
                if user is not None:
                        login(request,user)
                        resp= requests.post("https://userjwtauth.herokuapp.com/api/token/",
                        data={'email':email, 'password':password}).json()
                        token=(resp['access'])
                        customuser = CustomUser.objects.filter(email=email).first()
                        print(customuser.id)
                        customuser.token.user=customuser
                        customuser.token.token_key=token
                        customuser.save()
                        messages.success(request,'You have successfully Logined for 5 minutes')
                        return redirect('/')
                else:
                        messages.error(request,"username or password is incorrect")
                        return redirect('userapp:auth-login')
    return render(request,'userapp/signin.html')

@login_required(login_url='/login')
def listuserdetail(request):
        customuser=CustomUser.objects.get(id=request.user.id)
        resp=requests.get("https://userjwtauth.herokuapp.com/api/",headers={'Authorization':'Bearer '+customuser.token.token_key})
        if resp.status_code == HTTP_401_UNAUTHORIZED:
            logout(request)
            return redirect('login/')
        else:
            print(resp.json())
            return render(request,'userapp/index.html',{'response':resp.json()['result']})
        
        

class EditUserDetail(LoginRequiredMixin,UpdateView):
    model = CustomUser
    context_object_name='users'
    form_class = EditForm
    template_name='userapp/edit-detail.html'
    success_url = '/'

class DeleteUser(LoginRequiredMixin,DeleteView):
    model = CustomUser
    context_object_name='users'
    template_name='userapp/delete.html'
    success_url='/'
    success_message = "Deleted Successfully"

