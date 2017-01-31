
# Okay so I spent quite a few hgours on this and didn't make much progress.
# I know it's about spending time, so am sure I need to spend even more.
# I will annotate the two solutions I thought could work, but I couldn't really work.


# Solution 1 - My logic here was to create an object called experience and run the actual code for the steps required in that section called experience.

class experience(object):
    def __init__(self,Bicycle,Customer,Store):
        self.Bicycle=Bicycle
        self.Customer=Customer
        self.Store=Store
    
    print("Hi and welcome to the bike shop")
    
    # The idea I liked here was that I don;t want to have to do an if statement for each bike
    # I thought it would pass all the bikes through and print which one they could afford or not.
    
    if Bicycle >=Customer:
        print(Bicycle)
    else:
        print("There is no bike in your price range")

#this section is more defining the actual classes

class Bicycle(experience):
    def __init__(self, name, weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
        print(self.name)

bandit=Bicycle('Bandit',4,200)
rocker=Bicycle('Rocker',3,300)
dirt_rider=Bicycle('Dirt Rider',2,800)
fusion=Bicycle('Fusion',1.5,1000)
adder=Bicycle('Adder',2.5,600)
kentucky=Bicycle('Kentucky',5,190)

#this section is more defining the actual classes

class Customer(experience):
    def __init__(self,name,budget):
        self.name=name
        self.budget=budget
        
        print(self.name)
        print(self.budget)

john=Customer('John',600)
alex=Customer('Alex',400)
peter=Customer('Peter',300)

#this section is more defining the actual classes

class Store(experience):
    def __init__(self,name):
        self.name=name
        print (self.name)
    
store1=Store('Store1')
store2=Store('Store2')
store3=Store('Store3')
store4=Store('Store4')
store5=Store('Store5')
store6=Store('Store6')


# soluton2 - In this version I wanted to write the code below all the classes.

# Define the classes.

class Bicycle(object):
    def __init__(self, name, weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
        print(self.name)

bandit=Bicycle('Bandit',4,200)
rocker=Bicycle('Rocker',3,300)
dirt_rider=Bicycle('Dirt Rider',2,800)
fusion=Bicycle('Fusion',1.5,1000)
adder=Bicycle('Adder',2.5,600)
kentucky=Bicycle('Kentucky',5,190)



class Customer(object):
    def __init__(self,name,budget):
        self.name=name
        self.budget=budget
        
        print(self.name)
        print(self.budget)

john=Customer('John',600)
#alex=Customer('Alex',400)
#peter=Customer('Peter',300)


class Store(object):
    def __init__(self,name):
        self.name=name
        print (self.name)
    
store1=Store('Store1')
store2=Store('Store2')
store3=Store('Store3')
store4=Store('Store4')
store5=Store('Store5')
store6=Store('Store6')


# Now I didn;t want to put the functions within the different objects randomly.
# I wanted to write the code below but refer to the data which is classed above.








