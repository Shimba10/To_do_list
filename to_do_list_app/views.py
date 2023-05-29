from django.shortcuts import render
from templates import to_do_list_app

# Create your views here.
def home(request):
    if  request.GET.get('search_input'):
        return search_filter()
    return render(request,'to_do_list_app/home.html')