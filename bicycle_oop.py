
# objects

import random

class Bicycle(object):
    def __init__(self, name, weight,cost,sales_price):
        self.name = name
        self.weight = weight
        self.cost = cost
        self.sales_price=sales_price
    

class Customer(object):
    def __init__(self,name,budget):
        self.name=name
        self.budget=budget


class Store(object):
    def __init__(self, name,inventory):
        self.name=name
        self.inventory=inventory
    
    def sale(self,budget):
        
        # this will check to make sure that the bikes are in stock first.
        
        bikes_available=[]

        if self.inventory.get("bandit")>0:
            bikes_available.append(bandit)
        else:
            print()
            
        if self.inventory.get("rocker")>0:
            bikes_available.append(rocker)
        else:
            print()
            
        if self.inventory.get("dirt_rider")>0:
            bikes_available.append(dirt_rider)
        else:
            print()

        if self.inventory.get("fusion")>0:
            bikes_available.append(fusion)
        else:
            print()

        if self.inventory.get("adder")>0:
            bikes_available.append(adder)
        else:
            print()

        if self.inventory.get("kentucky")>0:
            bikes_available.append(kentucky)
        else:
            print()
        
        print('what is your budget', budget.name)
        print(budget.budget)
        
        # based on your budget you will be informed about all of the bikes that are available in the store.
        
        bike_short_list=[]
        
        if budget.budget > bikes_available[0].sales_price:
            print(bikes_available[0].name +' is in your price range and will cost you $' + str(bikes_available[0].sales_price))
            bike_short_list.append(bikes_available[0])

        if budget.budget > bikes_available[1].sales_price:
            print(bikes_available[1].name +' is in your price range and will cost you $' + str(bikes_available[1].sales_price))
            bike_short_list.append(bikes_available[1])

        if budget.budget > bikes_available[2].sales_price:
            print(bikes_available[2].name +' is in your price range and will cost you $' + str(bikes_available[2].sales_price))
            bike_short_list.append(bikes_available[2])

        if budget.budget > bikes_available[3].sales_price:
            print(bikes_available[3].name +' is in your price range and will cost you $' + str(bikes_available[3].sales_price))
            bike_short_list.append(bikes_available[3])     

        if budget.budget > bikes_available[4].sales_price:
            print(bikes_available[4].name +' is in your price range and will cost you $' + str(bikes_available[4].sales_price))
            bike_short_list.append(bikes_available[4])

        if budget.budget > bikes_available[5].sales_price:
            print(bikes_available[5].name +' is in your price range and will cost you $' + str(bikes_available[5].sales_price))
            bike_short_list.append(bikes_available[5])
        
        if budget.budget < (bikes_available[0].sales_price and bikes_available[1].sales_price and bikes_available[2].sales_price and bikes_available[3].sales_price and bikes_available[4].sales_price and bikes_available[5].sales_price):
            print("Sorry there are no bikes in your price range here. Please try our other stores")
        
        # the person will select a bike using the random function.
        
        bike_selected = random.choice(bike_short_list)
        
        print("Okay I think I will take the {}".format(bike_selected.name))
        
        # the remaining budget will be calculated
        
        remaining_budget = budget.budget - bike_selected.sales_price
        
        print("Your remaining budget is {}".format(remaining_budget))
        
        # we will work out how much inventory is left.
        
        print("this is the current inventory")
        print(self.inventory)
        
        self.inventory[bike_selected.name]-=1
        
        print("this is the remaining inventory")
        print(self.inventory)
        
        # the store profit will be calculated
        
        store_profit=bike_selected.sales_price-bike_selected.cost
        print("the store profit is $" + str(store_profit))


# actual data

bandit=Bicycle('bandit',4,200,200*1.2)
rocker=Bicycle('rocker',3,300,300*1.2)
dirt_rider=Bicycle('dirt_rider',2,1000,1000*1.2)
fusion=Bicycle('fusion',1.5,1000,400*1.2)
adder=Bicycle('adder',2.5,600,600*1.2)
kentucky=Bicycle('kentucky',5,190,190*1.2)

john=Customer('John',300)
alex=Customer('Alex',500)
peter=Customer('Peter',200)

inventory1={"bandit":1,"rocker":2,"dirt_rider":3}
inventory2={"dirt_rider":2,"fusion":7,"adder":3,"kentucky":1}
inventory3={"bandit":6,"rocker":5,"dirt_rider":8,"adder":3,"kentucky":3}
inventory4={"bandit":5,"rocker":2,"dirt_rider":1,"fusion":3,"adder":1,"kentucky":4}
inventory5={"bandit":4,"rocker":1,"dirt_rider":5,"fusion":4,"adder":1,"kentucky":7}
inventory6={"bandit":1,"rocker":1,"dirt_rider":6,"fusion":4,"adder":9,"kentucky":2}

store1=Store('Store1',inventory1)
store2=Store('Store2',inventory2)
store3=Store('Store3',inventory3)
store4=Store('Store4',inventory4)
store5=Store('Store5',inventory5)
store6=Store('Store6',inventory6)

# passing data through to the code to get a program

store6.sale(john)













