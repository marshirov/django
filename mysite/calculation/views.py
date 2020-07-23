from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.user)
    calc_dict = {'x':1, 'y':2, 'z':3}
    print(calc_dict)
    return render(request, 'calculation/list.html', {'calc_dict': calc_dict})
