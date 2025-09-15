#take gifts from the richest pile
import heapq
from typing import List

from numpy import floor, sqrt 
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #using max heap, as bydefualt python has min heap. And we need to get the max element each time
        #for each value of gift in gifts, we will invert the value and store in the heap list
        max_heap_gifts = [-gift for gift in gifts] #invert the values to use min-heap as max-heap, list comprehension
        heapq.heapify(max_heap_gifts) #transform/convert the list into a heap in-place
        
        for _ in range(k):
            richest_gift = -heapq.heappop(max_heap_gifts) #get the richest gift and invert back
            #new_gift = int(richest_gift**0.5) #take the square root and floor it
            #heapq.heappush(max_heap_gifts, -new_gift) #push the new gift back, inverted 
            heapq.heappush(max_heap_gifts, -floor(sqrt(richest_gift))) #push the new gift back, inverted
        
        return -sum(max_heap_gifts) #return the sum of remaining gifts, inverted back
    
#Example usage:
obj = Solution()
print(obj.pickGifts([25,64,9,4,100],4)) #29
print(obj.pickGifts([1,1,1,1],4)) #4
print(obj.pickGifts([10,10,10,10,10],5)) #15