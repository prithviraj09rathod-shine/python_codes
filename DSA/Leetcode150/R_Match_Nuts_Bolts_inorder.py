import sys
import random

def sort_nuts_and_bolts(nuts, bolts):
    """---------------------------------------------------------------------
> Documentation
Author:      Reshma Pawar
Date:        Sep. 18, 2025
Method:      sort_nuts_and_bolts(nuts, bolts)
Description: Sorts the nuts and bolts as described in Problem 3 on Test 1.
Input:       - The bucket of nuts
             - The bucket of bolts
Output:      - The sorted bucket of nuts
             - The sorted bucket of bolts
             
---------------------------------------------------------------------
    """

    if(len(nuts) <= 0 or len(bolts) <= 0):
        # base case
        return [],[]
    
    pivot_nut = nuts[0]
    less_than_pivot_nut_pile = []
    greater_than_pivot_nut_pile = []
    bolt_equal_to_nut = None

    for bolt in bolts:
        if bolt > pivot_nut:
            greater_than_pivot_nut_pile.append(bolt)
        elif bolt < pivot_nut:
            less_than_pivot_nut_pile.append(bolt)
        else:
            bolt_equal_to_nut = bolt
    
    pivot_bolt = bolt_equal_to_nut
    less_than_pivot_bolts_pile = []
    greater_than_pivot_bolts_pile = []
    
    for nut in nuts:
        if nut > pivot_bolt:
            greater_than_pivot_bolts_pile.append(nut)
        elif nut < pivot_bolt:
            less_than_pivot_bolts_pile.append(nut)

    nuts_arr = []
    bolts_arr = []

    lower_nuts, lower_bolts = sort_nuts_and_bolts(less_than_pivot_nut_pile, less_than_pivot_bolts_pile)
    if(len(lower_nuts) > 0):
        for (n, b) in zip(lower_nuts, lower_bolts):
            nuts_arr.append(n)
            bolts_arr.append(b)
    
    nuts_arr.append(pivot_nut)
    bolts_arr.append(bolt_equal_to_nut) 

    upper_nuts, upper_bolts = sort_nuts_and_bolts(greater_than_pivot_nut_pile, greater_than_pivot_bolts_pile)
    if(len(upper_nuts) > 0):
        for (n, b) in zip(upper_nuts, upper_bolts):
            nuts_arr.append(n)
            bolts_arr.append(b)
    

    return nuts_arr, bolts_arr


# boilerplate

if __name__ == "__main__":

    # print documentation
    #print sort_nuts_and_bolts.__doc__

    nuts = range(0, 25)
    bolts = range(0, 25)

    random.shuffle(nuts)
    random.shuffle(bolts)
    
    print ('Shuffled nuts: {0}'.format(nuts))
    print ('Shuffled Bolts: {0}'.format(bolts))

    
    n, b = sort_nuts_and_bolts(nuts, bolts)

    print ('Sorted nuts: {0}'.format(n))
    print ('Sorted Bolts: {0}'.format(b))
