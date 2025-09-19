
from typing import List

#2 pointer approach
class solution:
    def threesum(self, array: List[int]) -> List[List[int]]:
        print(array)
        array.sort()
        print("sorted array:")
        print(array)
        n = len(array)
        res = []

        for i in range(n-2):
            left = i+1
            right = n-1
            # Skip duplicate values for the first element
            if i > 0 and array[i] == array[i - 1]:
                continue


            while left < right :
                sum = array[i] +array [left] + array[right]
                if sum<0:
                    left +=1
                elif sum>0:
                    right-=1
                else:
                    res.append([array[i], array[left], array[right]])

                    # Skip duplicates for left and right
                    while left<right and array[left] == array[left+1]:
                        left+=1
                    while left<right and array[right] == array[right-1]:
                        right+=1

                    left+=1
                    right-=1
        return res

obj = solution()
nums = [-1,2,1,0,3,2,0]
print(obj.threesum(nums))
num1 = [-1, 0, 1, 2, -1, -4]
print(obj.threesum(num1))
