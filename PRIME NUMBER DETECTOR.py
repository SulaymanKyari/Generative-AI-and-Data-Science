#Prime number detector

def prime(number):
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
    print("Number is not prime")


