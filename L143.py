#Rosemary Hoffman and Krista Dockery
class Coffee_Mug:
    """Represents a coffee mug
    attributes: capacity, shape, material, color"""



mug=Coffee_Mug()
mug.capacity=12
mug.shape="cylinder"
mug.material="ceramic"
mug.color="pink"
mug.coffee=16
mug.drink=12

def coffee_drinking_simulation(x):
    a=mug.coffee-mug.drink
    print(a)


coffee_drinking_simulation(mug)
