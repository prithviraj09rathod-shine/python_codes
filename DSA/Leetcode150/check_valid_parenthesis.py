#2116. Check if a Parentheses String Can Be Valid
#We are given a string s, and the task is to check 
#whether the string consisting of only '(', ')' and '*' characters forms a valid sequence of parentheses. We consider '*' as a wildcard that can represent either '(', ')' or an empty string.

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1
        
        # Traverse the string from both ends simultaneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            # Count close parentheses or asterisks
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            # If at any point open count or close count goes negative, the string is invalid
            if open_count < 0 or close_count < 0:
                return False
        
        # If open count and close count are both non-negative, the string is valid
        return True
    
obj =Solution()
print(obj.checkValidString("(*)"))