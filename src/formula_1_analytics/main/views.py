from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import SearchForm


#def select_by_name(name: str):

#def select_by_name_lap_time(name: str, qlap_time: float):


def search(request):
    if request.method == 'POST':
        values_dict = request.POST.dict()
        values_dict.pop('csrfmiddlewaretoken', None)
        print(values_dict.values())
        for value in values_dict.values():
            if value != '':
                return render(request, 'main/search.html', {'values_dict': values_dict, 
                                                       })
                break                                                       
        

    return render(request, 'main/search.html', {})

def result(request):
    return render(request, 'main/result.html', {'values_dict': {},
                                               })