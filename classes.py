# -*- coding: utf-8 -*-
def check_degree(requirement):
    if requirement is None:
        degree = False
        return degree
    if "Высшее" in requirement:
        degree = True
    else:
        degree = False
    return degree


class vacancy():
    period = 1
    
    def fill_vacancy(self, name, area, address, employer, requirement, alternate_url):    
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
        #self.published_at = published_at // I'll add this later.
        #self.currency = currency