""" input = [1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]
o/p : true """
class Solution:
    def containsDuplicate0(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def containsDuplicate1(self, nums: list[int]) -> bool:
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def containsDuplicate2(self, nums: list[int]) -> bool:
        num_set = set()
        #print(num_set())
        for num in nums:
            print(num)
            if num in num_set:
                print(num)
                return True
            num_set.add(num)
        return False
    
    #Best single line code
    def containsDuplicate3(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    

print(Solution().containsDuplicate0([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))

