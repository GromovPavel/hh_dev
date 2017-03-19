# -*- coding: utf-8 -*-
def check_degree(requirement):
    if "Высшее" in requirement:
        degree = "True"
    else:
        degree = "Fasle"
    return degree

class vacancy():
    period = 1
    name = area = station_name = employer = requirement = alternate_url = is_open = degree =''
    
    def fill_vacancy(self, name, area, address, employer, requirement, alternate_url, published_at):    
        self.name = name
        self.area = area
        try:
            self.station_name = address['metro']['station_name']
        except:
            self.station_name = "None"
        self.employer = employer
        self.requirement = requirement
        self.degree = check_degree(requirement)
        self.alternate_url = alternate_url
        self.published_at = published_at