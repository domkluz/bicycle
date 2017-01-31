
import random

bike1={"Model name":"Bandit","Weight":4,"Cost to produce":200}
bike2={"Model name":"Rocker","Weight":3,"Cost to produce":300}
bike3={"Model name":"Dirt Rider","Weight":2,"Cost to produce":800}
bike4={"Model name":"Fusion","Weight":1.5,"Cost to produce":1000}
bike5={"Model name":"Adder","Weight":2.5,"Cost to produce":600}
bike6={"Model name":"Kentucy","Weight":5,"Cost to produce":190}


customer1={"Customer name":" John","budget":600}
customer2={"Customer name":" Alex","budget":400}
customer3={"Customer name":" Peter","budget":300}

uplift=1.2

bike1cost = bike1["Cost to produce"]*uplift
bike2cost = bike2["Cost to produce"]*uplift
bike3cost = bike3["Cost to produce"]*uplift
bike4cost = bike4["Cost to produce"]*uplift
bike5cost = bike5["Cost to produce"]*uplift
bike6cost = bike6["Cost to produce"]*uplift


store1={"Bandit":1,"Rocker":2,"Dirt Rider":3,"Fusion":4,"Adder":5,"Kentucy":6}
store2={"Bandit":3,"Rocker":5,"Dirt Rider":2,"Fusion":7,"Adder":3,"Kentucy":1}
store3={"Bandit":6,"Rocker":5,"Dirt Rider":8,"Fusion":7,"Adder":3,"Kentucy":3}
store4={"Bandit":5,"Rocker":2,"Dirt Rider":1,"Fusion":3,"Adder":1,"Kentucy":4}
store5={"Bandit":4,"Rocker":1,"Dirt Rider":5,"Fusion":4,"Adder":1,"Kentucy":7}
store6={"Bandit":1,"Rocker":1,"Dirt Rider":6,"Fusion":4,"Adder":9,"Kentucy":2}

bikeshortlist=[]

print("Hi and welcome to the bike shop...\n")

print("Hi customer{}\n".format(customer1['Customer name']))

print("What is your budget?\n")

print(customer1["budget"],"\n")

print("Okay these are your options that are available to you in this bike shop\n")

# can I create a variable from two strings

if customer1["budget"] >= bike1cost:
    print(bike1["Model name"],"cost ${}".format(bike1cost))
    bikeshortlist.append(bike1["Model name"])

if customer1["budget"] >= bike2cost:
    print(bike2["Model name"],"cost ${}".format(bike2cost))
    bikeshortlist.append(bike2["Model name"])

if customer1["budget"] >= bike3cost:
    print(bike3["Model name"],"cost ${}".format(bike3cost))
    bikeshortlist.append(bike3["Model name"])

if customer1["budget"] >= bike4cost:
    print(bike4["Model name"],"cost ${}".format(bike4cost))
    bikeshortlist.append(bike4["Model name"])

if customer1["budget"] >= bike5cost:
    print(bike5["Model name"],"cost ${}".format(bike5cost))
    bikeshortlist.append(bike5["Model name"])

if customer1["budget"] >= bike6cost:
    print(bike6["Model name"],"cost ${}".format(bike6cost))
    bikeshortlist.append(bike6["Model name"])
    
else:
    print("I'm sorry we don't have any bikes that meet your budget")

print("\nOkay let me take the following bike:\n")

inventory_draw_down = random.choice(bikeshortlist)

print(inventory_draw_down)

if bike1["Model name"]=="Bandit":
    print("That will be",bike1cost)
elif bike2["Model name"]=="Rocker":
    print("That will be",bike2cost)
elif bike3["Model name"]=="Dirt Rider":
    print("That will be",bike3cost)
elif bike4["Model name"]=="Fusion":
    print("That will be",bike4cost)
elif bike5["Model name"]=="Adder":
    print("That will be",bike5cost)
elif bike6["Model name"]=="Kentucy":
    print("That will be",bike6cost)
else:
    print("no bike selected")


print("You have left over {}".format(customer1["budget"]-(bike1cost or bike2cost or bike3cost or bike4cost or bike5cost or bike6cost)))

print("\n My stock is going from this level...\n")

print(store1)

store1[inventory_draw_down]-=1

print("\nTo this level!")

print("\n",store1)