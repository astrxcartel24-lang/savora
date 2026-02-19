from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def privacy(request):
    return render(request,'privacy.html')
def starter_page(request):
    return render(request,'starter_page.html')
def terms(request):
    return render(request,'terms.html')
def error(request):
    return render(request,'404.html')