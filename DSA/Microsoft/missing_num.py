from typing import List


class Solution:
    def missingNumber_xor(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    
    def missingNumber_verSum(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2      # n(n+1)//2 using formula
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    def missingNumber_hashSet(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    #did not understand this approach        
    def missingNumber_sort(self, nums: List[int]) -> int:
        nums.sort()
        ## Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0
        # If we get here, then the missing number is on the range (0, n)
        for i in range(1,len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
            
obj = Solution()
nums = [3,0,1]
print(obj.missingNumber_xor(nums))
print(obj.missingNumber_verSum(nums))
print(obj.missingNumber_hashSet(nums))
