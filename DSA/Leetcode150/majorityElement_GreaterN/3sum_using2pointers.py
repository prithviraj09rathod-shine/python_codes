#from pyparsing import nums
class solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        print(nums)
        
        #for i in range(n):
        for i, a in enumerate(nums):
            #remove duplicates
            if i>0 and a == nums[i-1]:
                continue
    
            left, right = i+1, len(nums)-1
            while left<right:
                threesum = a + nums[left] + nums[right]
                if threesum < 0:
                    left+=1
                elif threesum > 0:
                    right-=1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        return res
        

obj = solution()
nums = [-1,1,0,0,-1,2,3,4,5]
print(obj.three_sum(nums))
