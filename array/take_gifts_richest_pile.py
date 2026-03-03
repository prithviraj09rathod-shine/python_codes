import heapq
from typing import List
from math import sqrt, floor

class solution:
    def takegiftsfromRichestpile(self, gifts:List[int], k:int) :
        # Create a max heap by inverting the values
        max_heap_gifts = [-gift for gift in gifts]
        heapq.heapify(max_heap_gifts)

        #total_gifts_sum = 0

        for _ in range(k):
            # Extract the richest pile (invert back to positive)
            richest_pile = -heapq.heappop(max_heap_gifts)
            #total_gifts_sum += richest_pile

            # If there are remaining gifts, push them back into the heap
            heapq.heappush(max_heap_gifts, -floor(sqrt(richest_pile)))

        return -sum(max_heap_gifts)
    
obj = solution()
print(obj.takegiftsfromRichestpile([25,64,9,4,100],4))
# output 29 (how because after 4 operations the piles will be [5,8,9,4,3(sqrt(10))] sum is 29)
print(obj.takegiftsfromRichestpile([1,1,1,1],4)) #4
