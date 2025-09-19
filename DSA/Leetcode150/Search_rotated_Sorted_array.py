def search_rotated_array(nums, target):
    l , r = 0, len(nums) - 1

    while l <= r: # 4<=6, 4<=4
        mid = (l + r) // 2 # 3rd index which nums[mid]= 6, 4+6//2=5, 4+4//2=4

        if nums[mid] == target: # mid[3] = 6, nums[5]=1 ==0??, num[4]=0=target
            return mid

        # Left half is sorted
        if nums[l] <= nums[mid]: #num[l]=0< 1 ??? yes
            if nums[l] <= target < nums[mid]: #0<=0 <1 ??
                r = mid-1 # r=5-1=4, nums[4] r = mid-1 =5-1=4
            else:
        
                l = mid+1 # l=3+1=4->nums[4]=0
        
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[r]: #  6< 0 <2 ?
                r = mid - 1
            else:
                l = mid + 1

    return -1  # Target not found

array = [3,4,5,6,0,1,2] # 7,
target = 0
print(search_rotated_array(array, target))


