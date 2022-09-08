''' while True:
    try:
        n = int (input("please enter a number in range 1 to 100 : "))
        if n < 1 or n > 100:
            raise ValueError #this will send it to the print message and back to the input option
        break
    except ValueError:
        print("Invalid integer. The number must be in the range of 1-100.")
 '''
n = int (input())
for n in range(1 , n+1):
    # print( n ,". " ,"man khoshghlab hastam" , sep="")
    print("man khoshghlab hastam" , sep="")