""" while True:
    try:
        n = int(input('please enter a number in range 1 to 10 :'))
        if n < 1 or n > 10:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-10.")
 """
n =int(input()) 
print('W' , end="")
for i in range(1, n+1):
    print ("o" , end="")
print('w!' , end="")
    
    