from django.shortcuts import render

# Create your views here.
def download_method(request):
    return render(request,'download_method.html')