""" input = "A mam, a plan, a canal: Panama"
o/p : true """

class solution:
    def isPalindrome(self, s:str)->bool:
        l,r = 0,len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1    
        return True
    
    #short solution
    def isPalindrome1(self, s:str)->bool:
        print(s)
        #print(s.lower()) // converting to lower case
        #print(s.replace(" ","")) // removing spaces at the beginning
        s.lower().replace(" ","")
        print(s)
        return s==s[::-1]
#Example usage:
solution().isPalindrome
#str = ""
print(solution().isPalindrome1("MA D A M"))
print(solution().isPalindrome("Reshma"))

        