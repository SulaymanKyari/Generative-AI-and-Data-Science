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

