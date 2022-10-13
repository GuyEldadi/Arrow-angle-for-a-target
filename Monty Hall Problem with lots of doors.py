import random
maximumNumberOfDoors = int(input("What is the maximum amount of doors needed?: "))
n = int(input(f"How many iterations do you want of each variation from 3-{maximumNumberOfDoors} (Above 100 is recommended)?: "))
numberOfDoors = 3
with open('montyVar2.csv', 'w') as outFile:
    while numberOfDoors <=maximumNumberOfDoors:
        DOORS = []
        for k in range(numberOfDoors):
            DOORS.append(k)

        Stay = 0
        Switch = 0

        
        for k in range(n):
            # Choose the prize door
            prizeDoor = random.choice(DOORS)
            # Choose your door
            yourDoor = random.choice(DOORS)
            # Determine the door Monty Hall will open
            options = list(DOORS)
            options.remove(prizeDoor)
            if yourDoor in options:
                options.remove(yourDoor)
            montyDoor = random.choice(options)
            # Print out prizeDoor, yourDoor and montyDoor

            options = list(DOORS)
            options.remove(yourDoor)
            options.remove(montyDoor)
            otherDoor = random.choice(options)
            

            if prizeDoor==yourDoor:
                Stay+=1
            elif prizeDoor==otherDoor:
                Switch+=1

        Nothing = n - (Stay+Switch)
        print(f"{numberOfDoors}, {Nothing}, {Stay}, {Switch}", file = outFile)
        numberOfDoors+=1


