# Recursive function to calculate 
# the sum of numbers 0 - 15 

def recursive_sum(n):

    if n == 0 :
        return n
    
    else:
        return n + recursive_sum(n - 1)
    
output = recursive_sum(15)

print("The sum of numbers from 0 - 15 is: ", output)
