""" Here’s a clean and efficient implementation of Quick Sort in Python using the first element (array[low]) as the pivot. This version is great for understanding how partitioning works when the pivot is fixed at the start of the subarray.

Quick Sort Logic (Pivot = arr[low])
- Choose the first element as the pivot.
- Rearrange elements so that:
- All elements less than pivot are on the left.
- All elements greater than pivot are on the right.
- Recursively apply the same logic to left and right subarrays.
 """

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j



# Example Usage
arr = [24, 9, 29, 14, 19, 27]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


""" Output:
Sorted array: [9, 14, 19, 24, 27, 29]
 """