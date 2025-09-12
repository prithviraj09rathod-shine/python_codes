from typing import List
class Solution:
    def courseSchedule(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #preMap for each ccurse i, initiatlise it to its []empty list of prerequisites
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #visitSet = all the courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False #we have a cycle i.e we are visiting the same course again in the curr path
                #there we cant complte the courses
            if preMap[crs] == []: #no prerequisites therefore can take/complete this course
                return True #can complete this course
            

            visitSet.add(crs) #add to the curr path
            for pre in preMap[crs]: #for each prerequisite of the current course
                if not dfs(pre): #if we cannot finish even one of the prerequisite course, return false
                    return False
                
            visitSet.remove(crs) #remove from the curr path
            preMap[crs] = [] #mark as no prerequisites, so we don't need to do DFS next time
            return True
        
        for crs in range(numCourses):
             if not dfs(crs):
                return False    
        return True

#Example usage:
obj = Solution()
print(obj.courseSchedule(2, [[1,0]])) #True
print(obj.courseSchedule(2, [[1,0],[0,1]])) #False