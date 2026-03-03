from typing import List


class solution:
    def TwoSum(self, array: List[int], target: int) -> List[int] :
        seen_map = {}
        for i, num in enumerate(array):
            complement = target - num
            if complement in seen_map:
                return [seen_map[complement], i]
            seen_map[num] = i
        return []

    def Two_sum_using_two_pointer(self, array: List[int], target: int) -> List[int]:
        left, right = 0, len(array) - 1
        while left < right:
            current_sum = array[left] + array[right]
            if current_sum == target:
                return [left+1, right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
obj = solution()
print(obj.Two_sum_using_two_pointer([2,7,11,15],9))    
#print(obj.TwoSum([3,2,4],6))

print(obj.Two_sum_using_two_pointer([3,3],6))
#print(obj.TwoSum([3,2,3],6))
print(obj.Two_sum_using_two_pointer([1,5,3,4,5],10))