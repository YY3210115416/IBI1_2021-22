#I use Yin Yang as example, whose name is Yin Yang, location is International Campus, role is faculty.
class Staff(object):
    def __init__(self,first_name,last_name,location,role):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.role=role 
  
yy=Staff("Yin", "Yang", "International Campus", "faculty")
print(yy.first_name,yy.last_name,yy.location,yy.role)