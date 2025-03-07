from django.shortcuts import render, get_object_or_404
from .models import UserProfile
# Create your views here.

def users_list(request):
    users = UserProfile.objects.all()
    return render(request, 'users_list.html', {'users': users})
    
def user_detail(request,id):
    # product=get_product(id)
    user = get_object_or_404(UserProfile,id=id)
    return render(request,"user_detail.html",{"user":user})