
from typing import List
class solution:
    def canfinsih(self, numCourses:int, prerequisites: List[List[int]])->bool:
        #from collections import defaultdict, deque
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

