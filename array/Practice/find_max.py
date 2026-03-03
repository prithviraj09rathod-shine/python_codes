
class solution:
    def find_max(self, list1:list[int]) -> int:
        if not list1:
            return 0
        max_val = list1[0]
        for num in list1:
            if num > max_val:
                max_val = num
        return max_val
    
obj = solution()
#print(obj.find_max([3,1,4,1,5,9,2,6,5,3,5]))
print(obj.find_max([]))  # Edge case: empty list    