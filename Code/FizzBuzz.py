"""
Fizz and Buzz refer to any number that's a multiple of 3 and 5 respectively. In other words, if a number is divisible
by 3, it is substituted with fizz; if a number is divisible by 5, it is substituted with buzz. If a number is simultaneously
a multiple of 3 AND 5, the number is replaced with "fizz buzz."

"""

#solution

def FizzBuzz(lst, n):
    #lst - integer list
    #n - length of list

    
    
    #iterate 
    for i in range(n):
        #FizzBuzz
        if lst[i] % 3 == 0 and lst[i] % 5 == 0:
            lst[i] = "FizBuzz"

        #Fizz
        elif lst[i] % 3 == 0:
            lst[i] = "Fizz"

        #Buzz
        elif arr[i] % 5 == 0:
            lst[i] = "Buzz"

        else:
            lst[i] = lst[i]


    return lst

#driver code
arr = [int(x) for x in input().split()]
n = len(arr)
print(FizzBuzz(arr, n))
            
        

    
