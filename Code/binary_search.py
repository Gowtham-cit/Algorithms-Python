"""
->Binary search s basedon divide and conquer methohd.
->Faster than linear search
->The array should be sorted before searching

Assume we are searchong for the element X

This method will compare X to the middle of the element let sat middle

--> if middle is what we are looking for(middle==X) retuen the middle element positon

--> if not we decide the side by comparing middle is greater/lesser to X and omit the other side
   ** if middle is less than X then omt the left side vice versa

--> Repeat the steps untill find the element X

"""
def BinarySearch(lst, val):
    lst = sorted(lst)
    first = 0
    last = len(lst)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lst[mid] == val:
            index = mid
        else:
            if val<lst[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

lst = [int(x) for x in input().split()]
val = int(input())


print(f"{BinarySearch(lst, val)} is the position of the value in sorte list")



"""
Test case 1:

input:
4 6 3 4 2 1 7 8
2
output:
1 is the position of the value in sorted list


Test caase 2:

input:
88 77 44 66 771 98 36
66
output:
2 is the position of the value in sorte list
"""
