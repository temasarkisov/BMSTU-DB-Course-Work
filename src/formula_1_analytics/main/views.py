from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import SearchForm


#def select_by_name(name: str):

#def select_by_name_lap_time(name: str, qlap_time: float):


def search(request):
    if request.method == 'POST':
        keywords_dict = request.POST
        if keywords_dict:
            print(keywords_dict)
            return render(request, 'main/result.html', {'keywords_dict': keywords_dict.dict()})
        
        
        '''keywords_dict = {}

        for idx in range(4):
            keyword_type = (request.POST[f'keyword_type_{idx}'])
            keyword = request.POST[f'keyword_{idx}']
            keywords_dict[keyword_type] = keyword


        if keywords_dict:
            print(keywords_dict)
            return render(request, 'main/result.html', {'keywords_dict': keywords_dict})'''

    return render(request, 'main/search.html', {})

def result(request):
    return render(request, 'main/result.html', {})