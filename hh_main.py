# -*- coding: utf-8 -*-
import requests, json, sys
from classes import vacancy
from py_sql import insert

url = "https://api.hh.ru"
search_vacancies= "/vacancies/?" 
v_name = "text=System+administrator&"
v_count  = "per_page=400&"
v_with_salary = "only_with_salary=false"
v_area = "area=1&"
user_agent = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url + search_vacancies + v_name + v_area + v_count, v_with_salary, headers=user_agent)

if response.status_code == 400:
                print("Response error 400")
else:
                parsed_string = json.loads(response.content.decode('utf-8'))
                obj_vacancy = vacancy()
                for i in parsed_string['items']:
                                obj_vacancy.fill_vacancy(i['name'], i['area']['name'], i['address'], i['employer']['name'],
                                                         i['snippet']['requirement'], i['alternate_url'])
                                insert(obj_vacancy.name, obj_vacancy.area, obj_vacancy.station_name, 
                                       obj_vacancy.employer, obj_vacancy.requirement, obj_vacancy.alternate_url, obj_vacancy.degree)
       
       
#f = open('/home/gromov/Documents/project/hh_dev/f.txt', 'a')                        
#f.close()