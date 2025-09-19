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

# Test cases
arrays = [
    [4, 5, 6, 7, 0, 1, 2],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 1],
    [5, 6, 1, 2, 3, 4],
    [1]
]

for arr in arrays:
    print(f"Array: {arr} → Min: {find_min_rotated(arr)}")