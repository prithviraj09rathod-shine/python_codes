""" Here's a Python implementation of the Nuts and Bolts matching problem using Quick Sort, where the pivot is chosen as the first element (low) of the array. This version respects the constraint that comparisons can only be made between a nut and a bolt, not nut-to-nut or bolt-to-bolt.

🧠 Core Idea
- Use Quick Sort to match nuts and bolts.
- Pick a nut as pivot to partition bolts.
- Use the matched bolt to partition nuts.
- Recursively match subarrays.

🧾 Python Code (Pivot = low index) """
def partition(arr, low, high, pivot):
    i = low
    for j in range(low, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[low] = arr[low], arr[j]  # Move pivot to start
    arr[i - 1], arr[low] = arr[low], arr[i - 1]  # Place pivot correctly
    return i - 1

def match_nuts_and_bolts(nuts, bolts, low, high):
    if low < high:
        # Use nuts[low] as pivot to partition bolts
        pivot_index = partition(bolts, low, high, nuts[low])

        # Use matched bolt as pivot to partition nuts
        partition(nuts, low, high, bolts[pivot_index])

        # Recur for subarrays
        match_nuts_and_bolts(nuts, bolts, low, pivot_index - 1)
        match_nuts_and_bolts(nuts, bolts, pivot_index + 1, high)


#easiest way using hasmap
def match_nuts_bolts_hasmap(nuts, bolts):
    # Create a hash map for bolts
    bolt_map = {bolt: True for bolt in bolts}

    matched = []
    for nut in nuts:
        if nut in bolt_map:
            matched.append(nut)
            print(matched)

    #print(matched)
    # Sort for aligned output
    matched.sort()
    #nuts.sort()
    #bolts.sort()
    return matched, matched  # Nuts and bolts matched and sorted
    #return nuts, bolts  # Nuts and bolts matched and sorted

# Driver code
nuts  = ['@', '%', '$', '#', '^']
bolts = ['%', '@', '#', '$', '^']
#match_nuts_and_bolts(nuts, bolts, 0, len(nuts) - 1)
nuts_sorted,bolts_sorted =match_nuts_bolts_hasmap(nuts, bolts)

print("Matched nuts and bolts:")
print("Nuts:  ", nuts_sorted)
print("Bolts: ", bolts_sorted)



""" ✅ Output
Matched nuts and bolts:
Nuts:   ['#', '$', '%', '@', '^']
Bolts:  ['#', '$', '%', '@', '^'] """




