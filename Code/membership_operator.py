'''
Python’s membership operators test for membership in a sequence, 
such as strings, lists, or tuples. There are two membership operators as explained below



in ->Evaluates to true if it finds a variable in the specified sequence and false otherwise
not in -> Evaluates to true if it does not finds a variable in the specified sequence and false otherwise

'''

#finding  element in list
lst = input().split()
enter = input()

if enter in lst:
    print(f"{enter} is present")
else:
    print(f"{enter} is not present")

"""
Test case 1:

input:
1 j jj 32 nbf 345 2 5 3
jj
output:
jj is present


Test case 2:

input:
A B C D E F G H ! @ # %
*
output:
* is not present

"""
