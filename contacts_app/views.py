from importlib import reload
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
import random
from faker import Faker
from faker.providers import internet

# Create your views here.

def profile(request):
    faker = Faker([ 'en_US','en_IN'])
    profile2 = faker.profile()
    list_profile2 = profile2
    list_profile3 = []
    for i,j in list_profile2.items():
        list_profile3.append(str(i)+" : "+str(j))
    return render(request, 'index.html',{"list_profile2":list_profile3})
    
#['it_IT', 'en_US', 'ja_JP','hi_IN']