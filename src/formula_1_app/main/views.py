from django.http.response import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.models import User

import json
import requests


TEMPLATE_LOGIN = 'main/login.html'
TEMPLATE_USER_SETTINGS = 'main/user_settings.html'
TEMPLATE_SIGN_UP = 'main/sign_up.html'
TEMPLATE_SEARCH = 'main/search.html'

#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------  

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

        return render(request, TEMPLATE_SIGN_UP)

#------------------------------------------------------------------------------

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

                return render(request, TEMPLATE_SEARCH, {'result_list': result_list})                  

    if request.user.is_authenticated:
        return render(request, TEMPLATE_SEARCH)
    else:
        return render(request, TEMPLATE_SEARCH, {'error': 'User was not authenticated'})

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

#------------------------------------------------------------------------------

def user_settings(request):
    username = request.user.username
    user = User.objects.get(username__exact=username)
    password = user.password
    email = user.email
    is_superuser = user.is_superuser

    users = User.objects.all()
    users_info_list = []
    for user in users:
        users_info_list.append([user.id, user.is_superuser, user.username, user.email])

    if request.method == 'POST':
        if not is_superuser:
            new_email = request.POST['value_new_email_to_change']
            password_to_confirm = request.POST['value_password_to_change']

            if new_email != email and check_password(password_to_confirm, password):
                user.email = new_email
                user.save()
                
                return render(request, TEMPLATE_USER_SETTINGS, {'username': user.username, 'email': user.email, 'is_superuser': is_superuser})

        if is_superuser:
            username_to_delete = request.POST['value_username_to_delete']
            password_to_delete = request.POST['value_password_to_delete']

            try:
                user_to_delete = User.objects.get(username__exact=username_to_delete)
            except:
                return render(request, TEMPLATE_USER_SETTINGS, {'username': user.username, 'email': user.email, 'is_superuser': is_superuser, 'users_info_list': users_info_list})
            
            if user_to_delete and check_password(password_to_delete, password):
                user_to_delete.delete()
                users = User.objects.all()
                users_info_list = []
                for user in users:
                    users_info_list.append([user.id, user.is_superuser, user.username, user.email])
                
                return render(request, TEMPLATE_USER_SETTINGS, {'username': user.username, 'email': user.email, 'is_superuser': is_superuser, 'users_info_list': users_info_list})
    
    if not is_superuser:
        return render(request, TEMPLATE_USER_SETTINGS, {'username': username, 'email': email, 'is_superuser': is_superuser})
    if is_superuser:
        return render(request, TEMPLATE_USER_SETTINGS, {'username': username, 'email': email, 'is_superuser': is_superuser, 'users_info_list': users_info_list})
    
    return render(request, TEMPLATE_USER_SETTINGS, {'error': 'Something went wrong :('})

