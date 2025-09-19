
from typing import List


class solution:
    def prod_max1_min2_arrays(self, array1:List[int], array2:List[int])->int:
        n1 = sorted(array1)
        n2 = sorted(array2)
        prod = n1[-1] * n2[0]
        print(prod)
        return prod
    
obj = solution()
array1 = [1,2,7,3,4]
array2 = [1,3,5,2,7]
print(obj.prod_max1_min2_arrays(array1, array2))
    
