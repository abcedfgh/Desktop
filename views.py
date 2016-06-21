from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .models import rrj
from django.utils import timezone
from django.template.loader import get_template
from django.template import Context
from .forms import PostForm
from django.views.generic import View

import time
# Create your views here.


def game(request):

   
    num = range(0, 101)
    b = num[0]
    l = num[100]
    mid = (b + l) / 2
    return render(request,'blog22/js.html',{'mid':mid})

def gameg(request):
    b=mid
    mid=(b+l)/2
    return render(request,'blog22/gameg.html',{'mid':mid})

def gamel(request):
    l=mid
    mid=(b+l)/2
    return render(request,'blog22/gamel.html',{'mid':mid})


   
