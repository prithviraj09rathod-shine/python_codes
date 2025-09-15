class solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0

        return max_sum
    
    def maxSubArray1(self, nums):
        max_sum = float('-inf')
        current_sum = 0 
        ansStart = -1
        ansEnd = -1
        start = 0

        for num in nums:
            if current_sum == 0:
                start = nums.index(num)
            
            current_sum += num
          
            if(current_sum > max_sum):
                max_sum = current_sum
                ansStart = start
                ansEnd = nums.index(num)
            
            if current_sum < 0:
                current_sum = 0
            print(f"Subarray indices: start={ansStart}, end={ansEnd}")  
        return max_sum
    
obj = solution()
print(obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) #6
print(obj.maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])) #6
#Output: Subarray indices: start=3, end=6
#Output: 6
print(obj.maxSubArray([-1])) #-1