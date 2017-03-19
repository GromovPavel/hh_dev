# -*- coding: utf-8 -*-
def check_degree(requirement):
    if "Высшее".decode('utf-8'):
        degree = "True"
    else:
        degree = "Fasle"
    return degree

class vacancy():
    period = 1
    name = area = station_name = employer = requirement = alternate_url = is_open = degree =''
    def fill_vacancy(self, name, area, address, employer, requirement, alternate_url, is_open):    
        
        self.name = name.encode(encoding='utf-8')
        self.area = area.encode(encoding='utf-8')
        try:
            self.station_name = address['metro']['station_name'].encode(encoding='utf-8')
        except:
            self.station_name = "None"
        self.employer = employer.encode(encoding='utf-8')
        self.requirement = requirement
        self.alternate_url = alternate_url.encode(encoding='utf-8')
        self.is_open = is_open.encode(encoding='utf-8')
        self.degree = check_degree(requirement)
        
        #area, station_name, employer, requirement, alternate_url