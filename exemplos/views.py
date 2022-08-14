from django.shortcuts import render


# Create your views here.
def get_bootstap(request):

    return render(request, 'exemplo/02_container.html')
