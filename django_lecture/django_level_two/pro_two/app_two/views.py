from django.shortcuts import render
from app_two.models import User

# Create your views here.

def index(request):
    return render(request,'app_two/index.html')

def user(request):
    userpage_list = User.objects.order_by('first_name')
    user_rec = {"users_record":userpage_list}
    return render(request,'app_two/user.html',context=user_rec)