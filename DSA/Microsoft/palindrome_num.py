class solution:
    def check_palindrome(self, num:int)->bool:
        if num < 0:
            return False
        str_num = str(num)
        l, r = 0, len(str_num) - 1
        while l < r:
            if str_num[l] != str_num[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def palindrome_short(self, num:int)->bool:
        str_num = str(num)
        return str_num == str_num[::-1]
    
    
#Example usage:
obj = solution()
print(obj.check_palindrome(121))  # True
print(obj.check_palindrome(-121)) # False
print(obj.check_palindrome(10))   # False
print(obj.check_palindrome(12321))# True

