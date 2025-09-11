class solution:
    def removeDuplicates(self, string1: str) -> str:
            if len(string1) != len(set(string1)) :
                print("Duplicates found")
                return str(set(string1))
            else:
                print("No duplicates found")
                return string1

    def removeDuplicateChars(self, string1: str) -> str:
            result =""
            string_set = set()
            #print(string_set())
            for char in string1:
                #print(char)
                if not char in string_set:
                    string_set.add(char)
                    result+=char       
            return result  

    def removeDuplicateChars2(self, string1: str) -> str:
            result =""
            string_set = set()
            for char in string1:
                #print(char)
                if not char in string_set:
                    string_set.add(char)
                    result+=char       
            return result   

#print(solution().removeDuplicates("Reshma"))
#print(solution().removeDuplicateChars("banana")) 
print(solution().removeDuplicateChars2("banana"))   