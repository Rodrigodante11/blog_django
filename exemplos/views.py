from django.shortcuts import render


# Create your views here.
def get_bootstap(request):
    print("chegou aqui")
    return render(request, 'exemplo/05_grid.html')

