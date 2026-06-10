from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def shop(request):
    return render(request, 'main/shop.html')