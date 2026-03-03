#using binary search o(logn) and o(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

def find_min_rotated(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]

#Better Approach using binary search and similar to rotated sorted array minimum element
#https://www.youtube.com/watch?v=nhEMDKMB44g
#TRied and owrked for me
def find_min_rotated_v2(arr):
    left, right = 0, len(arr) - 1
    ans = float('inf') # INT_MAX

    while left <= right: #<= to handle case when only one element is there
        mid = (left + right) // 2

        #if left half is sorted
        if arr[left] <= arr[mid]: #<= to handle case when only two elements are there
            ans = min(ans, arr[left])
            left = mid + 1 # delete left half
        else: # right half is sorted
            ans = min(ans, arr[mid])
            right = mid - 1 # delete right half
    return ans

# Test cases
arrays = [
    [4, 5, 6, 7, 0, 1, 2],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [5, 6, 1, 2, 3, 4],
    [1]
]

for arr in arrays:
    #print(f"Array: {arr} → Min: {find_min_rotated(arr)}")
    print(f"Array: {arr} → Min (v2): {find_min_rotated_v2(arr)}")