class solution:
    def mergesort(arr:list[int], low:int, high:int):
        if low >= high:
            return
        mid = low + high/2
        
        mergesort(low,mid)
        mergesort(mid+1,high)
        merge(arr, low, mid, high)
        
    def merge(arr:list[int], low:int, mid:int, high:int):
        temp = []
        left, right  = low, mid+1
        n = len(arr)

        while left<=mid and right <=high:
            if arr[left]<=arr[right] :
                temp.add(arr[left])
                left+=1
            else:
                temp.add(arr[right])
                right+=1

        while left<=mid:
            temp.add(arr[left])
            left +=1
        while right <=high:
            temp.add(arr[right])
            right +=1

        for i in range(n):
            arr[i] = temp[i-low]
            


        

