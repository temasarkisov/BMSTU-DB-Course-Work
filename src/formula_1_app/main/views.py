from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings


import json
import requests


def value_to_cut_value(value: str) -> str:
    return value.replace('_', '+').replace('-', '\-')


def links_values_to_request(links_list: list, values_list: list) -> str:
    if len(links_list) == len(values_list):
        cube_request_cut = ''
        for i in range(len(links_list)):
            if i == 0:
                cube_request_cut += f'{links_list[i]}:{value_to_cut_value(values_list[i])}'
            else:
                cube_request_cut += f'|{links_list[i]}:{value_to_cut_value(values_list[i])}'
        
        return f'http://localhost:5000/cube/result/facts?cut={cube_request_cut}'
    
    return ''

def search(request):
    if request.method == 'POST':
        values_dict = request.POST.dict()
        values_dict.pop('csrfmiddlewaretoken', None)

        with open (f'{settings.BASE_DIR}/main/static/main/links/links.json') as links_file:
            links_dict = json.load(links_file)

        links_values_dict = {}
        links_list = []
        values_list = []
        for _, key in enumerate(values_dict):
            if (values_dict[key] != ''):
                links_list.append(links_dict[key])
                values_list.append(values_dict[key])
                links_values_dict[links_dict[key]] = values_dict[key]

        #print(links_values_dict)

        if links_values_dict:
            cube_request = links_values_to_request(links_list, values_list)
            result_dicts_list = requests.get(cube_request).json()
            print(result_dicts_list[0])
            result_list = []
            for result_dict in result_dicts_list:
                result_list.append([result_dict['__fact_key__'],
                                    result_dict['driver.forename'],
                                    result_dict['driver.surname'],
                                    result_dict['race.name'],
                                    result_dict['race.date'],
                                    result_dict['number'],
                                    result_dict['grid'],
                                    result_dict['position'],
                                    result_dict['position_order'],
                                    result_dict['laps'],
                                    result_dict['points'],
                                    result_dict['fastest_lap_speed'],
                                    ])
            print(result_list[0])

            return render(request, 'main/search.html', {'result_list': result_list, 
                                                       })                                         

    return render(request, 'main/search.html', {'result_list': {},
                                               })

def result(request):
    return render(request, 'main/result.html', {'result_list': {},
                                               })

def login(request):
    return render(request, 'main/login.html', {})