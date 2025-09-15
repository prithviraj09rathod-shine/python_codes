#using Moore Voting Algorithm for finding majority element which appears more than n/2 times
class solution:
    def majorityElement(self, nums:list) ->int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                count = 1
                candidate = num
            count += (1 if num == candidate else -1)
            print(f"Current number: {num}, Count: {count}, Candidate: {candidate}")

        cnt1 = 0
        for num in nums:
            if num == candidate:
                cnt1+=1
        if cnt1>len(nums)/2:
            return candidate
        return -1
    
#example usage
obj = solution()
nums = [1,2,3,4,5,1,1,1,6]
print(obj.majorityElement(nums))
nums1 = [2,2,2,2,2,1,1,1]
result = obj.majorityElement(nums1)
print(result)
    
