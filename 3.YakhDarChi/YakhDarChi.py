''' while True:
    try:
        T = int(input("please enter a number in range -273 to 6000 : "))
        if T < -273 or T > 6000:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of -273-6000.") '''
        
T = int(input())   

if T < -273 :
    if T > 6000:
        print("error")

else:
    if -273 < T < 0 :
        print("Ice")
                 
    elif 100 < T < 6000 :
        print("Steam")
    
    else:
        print("Water")

