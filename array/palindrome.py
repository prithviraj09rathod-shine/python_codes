
class solution:
    def __init__(self):
        pass

class NodeList:
    def __init(self, val=0, next=None):
        self.val = val
        self.next = next

    def palindrome(self, array:list[int])->bool:
        print(array)
        n = len(array)
        left, right = 0, n-1

        while left < right :
            if array[left] != array[right]:
                return False   
            left += 1
            right -=1
        return True
    
    #short solution
    def palindrome_array(self, nums:list[int])->bool:
        print(nums)
        return nums==nums[::-1]
obj = solution() # object creation=initialization
#print(obj.palindrome_array([4,5,1,5,4]))
print(obj.palindrome([5,5,5,5,5]))

