class solution:
    def decodestring(self,s:str)-> str:
        stack = []

        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] !="[":
                    substr = stack.pop()+substr
                    print(substr)
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                    print(k)
                    stack.append(int(k)*substr)
        return "".join(stack)
    
s = "54[ab6[cd]]"
obj = solution()
print(obj.decodestring(s))