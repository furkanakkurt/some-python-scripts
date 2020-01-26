def addCar(plateNumber, ownerName):
    if plateNumber not in cars:
        cars[plateNumber] = []
        cars[plateNumber].append(ownerName)
        print("Car added successfuly ")
    else:
        print("Car already exists ")

def updateCar(plateNumber, ownerName):
    if plateNumber in cars:
        cars[key].append(ownerName)
    else:
        print("No such plate number is found ")


def findCar(plateNumber):    
    try:
        return cars[plateNumber]
    except KeyError:
        print("No such plate number is found! ")
        return None


cars = {}
choice = int(input('1)Add Car\n2)Search Car\n3)Update Owner\n4)Quit\nEnter Choice:'))
while choice != 4:
    
    if choice == 1:
        plateNo = input('Enter plate number: ')
        owner = input('Enter name of owner: ')
        addCar(plateNo, owner)
        
    elif choice == 2:
        plateNo = input('Enter plate number: ')
        car = findCar(plateNo)
        if car != None:
            print("List of previous owners: "+str(car))
    elif choice == 3:
        plateNo = input('Enter plate number: ')
        if plateNo in cars:
            owner = input('Enter name of owner to add: ')
            updateCar(plateNo, owner)
        else:
            print("No such plate number is found ")
    else:
        print('Invalid choice')
    
    choice = int(input('1)Add Car\n2)Search Car\n3)Update Owner\n4)Quit\nEnter Choice:'))
print('Program Ended....')
