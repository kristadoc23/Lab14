#Krista Dockery and Rosemary Hoffman
class Ambulance:
    """Represents an ambulance
    attributes: logo,sound,lights,color,patients"""

truck=Ambulance()
truck.logo="hospital"
truck.sound="siren"
truck.lights="red"
truck.color="white"
truck.patient=3


print(type(Ambulance))

def speed(x,y):
    if x.patient==0:
        print("speed is the same as traffic flow")
    else:
        speed=2.3*(x.patient-0.5)*y+30*(x.patient-2.143)
        print("speed is",speed)


speed(truck,15)
