# -*- coding: utf-8 -*-
import requests, json, sys
from classes import vacancy

url = "https://api.hh.ru"
search_vacancies= "/vacancies/?" 
v_name = "text=System+administrator&"
v_count  = "per_page=50&"
v_with_salary = "only_with_salary=true"
v_area = "area=1&"
user_agent = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url + search_vacancies + v_name + v_area + v_count, v_with_salary, headers=user_agent)

parsed_string = json.loads(response.content)

z = 0

obj_vacancy = vacancy()
f = open('/home/gromov/Documents/hh/f.txt', 'a')


for i in parsed_string['items']:
                obj_vacancy.fill_vacancy(i['name'], i['area']['name'], i['address'], i['employer']['name'],
                                         i['snippet']['requirement'], i['alternate_url'], i['type']['name'])
                
                f.write(obj_vacancy.name + ' ' + obj_vacancy.area + ' ' + obj_vacancy.station_name + ' ' + obj_vacancy.employer + ' ' +
                        obj_vacancy.degree + ' ' + obj_vacancy.alternate_url + ' ' + obj_vacancy.is_open + '\n')        
        


#f.write(obj_vacancy.name + ' ' + obj_vacancy.area + ' ' + obj_vacancy.station_name + ' ' + obj_vacancy.employer + ' ' +
        #obj_vacancy.degree + ' ' + obj_vacancy.alternate_url + ' ' + obj_vacancy.is_open + '\n')


#print(obj_vacancy.name, obj_vacancy.area)

f.close()