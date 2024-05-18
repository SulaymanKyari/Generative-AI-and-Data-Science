#Prime number detector

"""def prime(number):
    '''Function  is set to detect prime numbers'''
    if number <= 1 :
        return False
    
    elif number == 2 :
        return True
    
    elif number % 2 == 0 :
        return False
    
    else:
        for i in range(3, int(number**0.5) + 1, 2) :
            if number % i == 0:
                return False
            return True

number = int(input("Enter a number: "))

if prime(number):
    print("Number is prime")

else:
    print("Number is not prime")"""


# Print numbers 1-100, FIZZ for multiples of 3, BUZZ for multiples of 5 
# and FIZZBUZZ for multiples of 3 and 5

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    
    elif i % 3 == 0:
        print("FIZZ")
    
    elif i % 5 == 0:
        print("BUZZ")
    
    else:
        print(i)

