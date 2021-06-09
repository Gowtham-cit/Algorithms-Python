"""
Linear search is one of the simplest searching algorithms, 
and the easiest to understand. We can think of it as a ramped-up version of o
ur own implementation of Python's in operator

"""
#return the position of the element if available


def LS(lst, find):
    
    for i in range(len(lst)):
        if lst[i] == find:
            return i
    return 0
lst = [int(x) for x in input().split()]
find = int(input())

ans = LS(lst, find)
if ans:
    print(f"{ans} is the position of the element")
else:
    print("Oops...! Not found anything")

"""
Test case 1:

input:
1 2 3 4 5  6 7 8
3
output:
2 is the position of the element


Test case 2:

input:
1 2 3 4 5  6 7 8
0
output:
Oops...! Not found anything

"""
