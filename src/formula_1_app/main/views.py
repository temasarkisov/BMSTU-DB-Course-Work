from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User

import json
import requests


TEMPLATE_LOGIN = 'main/login.html'
TEMPLATE_REGISTER = 'main/sign_up.html'
TEMPLATE_SEARCH = 'main/search.html'


class LoginView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        context = {}
        if request.method == 'POST':
            username = request.POST['value_username']
            password = request.POST['value_password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('../search/')
            else:
                context['error'] = 'Incorrect login or password'
        return render(request, TEMPLATE_LOGIN, context)
    

class SignUpView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('value_username')
            email = request.POST.get('value_email')
            password = request.POST.get('value_password')
            password_confirm = request.POST.get('value_password_confirm')

            if password == password_confirm:
                User.objects.create_user(username, email, password)
                return redirect(reverse("login"))

        return render(request, TEMPLATE_REGISTER)


def search(request):
    if request.user.is_authenticated:
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

                return render(request, 'main/search.html', {'result_list': result_list})                  

    if request.user.is_authenticated:
        return render(request, 'main/search.html')
    else:
        return render(request, 'main/search.html', {'error': 'Please login to use Formula 1 Analyser'})

def result(request):
    return render(request, 'main/result.html', {'result_list': {},
                                               })

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


'''class SearchView():
    def search(self, request):
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
                cube_request = self.__links_values_to_request(links_list, values_list)
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

    def __value_to_cut_value(self, value: str) -> str:
        return value.replace('_', '+').replace('-', '\-')


    def __links_values_to_request(self, links_list: list, values_list: list) -> str:
        if len(links_list) == len(values_list):
            cube_request_cut = ''
            for i in range(len(links_list)):
                if i == 0:
                    cube_request_cut += f'{links_list[i]}:{self.__value_to_cut_value(values_list[i])}'
                else:
                    cube_request_cut += f'|{links_list[i]}:{self.__value_to_cut_value(values_list[i])}'
            
            return f'http://localhost:5000/cube/result/facts?cut={cube_request_cut}'
        
        return '' '''