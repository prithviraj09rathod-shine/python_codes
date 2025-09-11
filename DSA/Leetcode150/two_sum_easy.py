#Given array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
from typing import List

#better approach using hashmap
class solution:
    def twoSum(self, nums:List[int], target:int)->list[int]:
        hashmap_seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap_seen:
                print("hashmap_seen:")
                print(hashmap_seen)
                return [hashmap_seen[complement], i]
            hashmap_seen[nums[i]] = i
            print("hashmap_seen outside if block:")
            print(hashmap_seen)
        return []

#traditional brute force approach
class solution1:
    def twoSum1(self, nums:List[int], target:int)->list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                return []

#best way using two pointer approach for already sorted array.   
class solution2:
    def twoSum2(self, nums:List[int], target:int)->list[int]:
       l, r = 0, len(nums) - 1
       while(l<r):
           currSum = nums[l]+nums[r]
           if currSum < target:
               print("Increasing left pointer")
               l += 1
           elif currSum > target:
               print("Increasing right pointer")
               r -= 1 
           else:
                print("Returning indicses")
                return [l+1, r+1]       

#Example usage:instantiate the class and call the method
obj = solution()
obj1 = solution1()
obj2 = solution2()
print("Executing hashmap approach")
print(obj.twoSum([2,7,11,15],9)) #[0,1]
print("Executing brute force approach")
print(obj1.twoSum1([2,7,11,15],9)) #[0,1](brute force)
print("Executing two pointer approach")
print(obj2.twoSum2([3,2,4],6)) #[1,2]// in this case this logic not working as array is not sorted
print(obj2.twoSum2([2,7,11,15],9)) #[0,1] (two pointer approach)