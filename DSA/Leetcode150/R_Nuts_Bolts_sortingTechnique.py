def partition(arr, low, high, pivot):
    i = low
    for j in range(low, high):
        print(arr[i])
        print(arr[j])
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def match_nuts_and_bolts(nuts, bolts, low, high):
    if low < high:
        # Choose last bolt as pivot to partition nuts
        #partition_index = partition(arr, low, hig, arr[low])
        pivot_index = partition(nuts, low, high, bolts[high])

        # Use matched nut as pivot to partition bolts
        #extra line in case of " matching nuts and bolts" as we have 2 arrays here
        partition(bolts, low, high, nuts[pivot_index])

        # Recur for subarrays, comparing with qs code in comments
        #qs(arr,low,partition-1)
        match_nuts_and_bolts(nuts, bolts, low, pivot_index - 1)
        #qs(arr,partition+1, high)
        match_nuts_and_bolts(nuts, bolts, pivot_index + 1, high)

# Driver code
nuts  = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']
nuts_sorted, bolts_sorted = match_nuts_and_bolts(nuts, bolts, 0, len(nuts) - 1)

print("Matched nuts and bolts:")
print("Nuts:  ", nuts_sorted)
print("Bolts: ", bolts_sorted)
#print("Nuts:  ", nuts_sorted)
#print("Bolts: ", bolts_sorted)


