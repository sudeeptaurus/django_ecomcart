from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Index Blog")
    return render(request, 'blog/index.html')

def blogpost(request):
    # return HttpResponse("Blog Posts")
    return render(request, 'blog/blogpost.html')