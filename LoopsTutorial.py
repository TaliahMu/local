def collatz(number):
    # Is the mod of 2 equal to 0?
    if number % 2 == 0:
        result = number/2
        print (result)
        return result

    # If the mod of 2 isn't equal to 0, print `3 * number + 1`
    elif number % 2 == 1:
        
        print (1+number*3)
        return 1+number*3
        

# Ask input from the user    
n = input()

# As long as `n` is not equal to `1`, run `collatz()`
while n != 1:
    n = collatz(int(n))

number = int(input('number = '))
while number < 5:
    while number%2==0:
        print ('the number ' + str(number) + ' is even')
        break
    print(str(number) + ' is less than 5')
    break
#okay im really done
    #syke
for number in range(3) :  
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    
    for another_number in range(3):
        print("****************************")
        print("I am inner loop iteration "+str(another_number))
        break

