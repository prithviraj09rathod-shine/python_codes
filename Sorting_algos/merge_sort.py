class solution:
    def mergesort(self,arr:list[int], low:int, high:int):
        if low >= high:
            return
        mid = low + high/2
        
        mergesort(low,mid)
        mergesort(mid+1,high)
        merge(arr, low, mid, high)
        
    def merge(self, arr:list[int], low:int, mid:int, high:int):
        temp = []
        left, right  = low, mid+1
        n = len(arr)

        while left<=mid and right <=high:
            if arr[left]<=arr[right] :
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1

        while left<=mid:
            temp.append(arr[left])
            left +=1
        while right <=high:
            temp.append(arr[right])
            right +=1

        for i in range(n):
            arr[i] = temp[i-low]
            
obj = solution()
arr = [38,27,43,3,9,82,10]
obj.mergesort(arr, 0, len(arr)-1)
print("Sorted array is:", arr)


        

