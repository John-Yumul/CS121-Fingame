
def conversion ():
    int (net_worth)
    int (energy)
    int (health)
    int (fun)

def tasks ():                                #Add Job increase in money
    print("[1] Food")
    print("[2] Leisure")
    print("[3] Exercise")
    print("[4] Transportation")
    print("[0] Exit")
    
def food ():                                #Simplify print
    
    print("FOOD")
    print("[1] Home Cooking")
    print("[2] Take-Out / Delivery")
    print("[3] Karinderya")
    print("[4] Fast Food")
    print("[5] Fine Dining")
    print("[0] Exit")
    
    option = int(input("Enter your option: "))
    

    if option == 1:                             #Edit amount of stats
        deets()
        net_worth = int(net_worth)
        print(type(net_worth))

        '''
        net_worth -= 1
        energy -= 1
        health -= 1
        fun -= 1
        for x in stats:
            print(x)
        '''

    elif option == 2:
    
        print("Option 2 has been called.")
            
    elif option == 3:
    
        print("Option 3 has been called.")
            
    elif option == 4:
    
        print("Option 4 has been called.")
    
    else:
    
        print("Invalid option.")
    
        print()
        tasks()
        option = int(input("Enter your option: "))
        
    
    
    
    
def leisure ():  
    print("LEISURE")
    print("[1] Cinema")
    print("[2] Meet Friends")
    print("[3] Concert")
    print("[0] Exit")
    
def exercise ():       
    print("EXERCISE")
    print("[1] Running")
    print("[2] Swimming")
    print("[3] Bicycle")
    print("[4] Gym")
    print("[0] Exit")

def transportation ():
    print("TRANSPORTATION")
    print("[1] Walking")
    print("[2] Car")
    print("[3] Jeepney")
    print("[4] Grab")
    print("[0] Exit")


def deets ():
    net_worth = "10000"
    energy = "100"
    health = "100"
    fun = "100"
    stats = ["Net Worth: " + net_worth + " Php", "Energy: " + energy + "%", "Health: " + health + "%", "Fun: " + fun + "%", "Status: "]

for x in stats:
  print(x)
 


tasks()
option = int(input("Enter your option: "))

decision = 5

while option != 0:
    if option == 1:
        food()
       
        
        
        #decision -= 1
        #print(decision)

    elif option == 2:

        print("Option 2 has been called.")
        
    elif option == 3:

        print("Option 3 has been called.")
        
    elif option == 4:

        print("Option 4 has been called.")

    else:

        print("Invalid option.")

    print()
    tasks()
    option = int(input("Enter your option: "))
    
print("Thank you.")

