# Search target in Rotated sorted array
from typing import List

def serach_inRotated_SortedArray(array:List[int], target:int):
    l, r = 0, len(array)-1
    
    while l<=r:
        mid = (l+r)//2 ### very mip to put bracket otherwise code will hang

        if target == array[mid]:
            return mid
            
        #Either Left half will be sorted or riht half. So If left haf is sorted
        #below code works
        if array[l] <= array[mid]:
            if array[l] <= target and target < array[mid]:
                r = mid-1
            else:
                l=mid+1
        else:
            if array[mid]< target and target <=array[r]:
                l=mid+1 
            else:
                r=mid-1
    return -1
    
array = [3,4,5,6,7,0,1,2]
target = 0
print(serach_inRotated_SortedArray(array, target))