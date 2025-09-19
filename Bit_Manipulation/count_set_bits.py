def count_set_bits_rightshifting(n:int):
    count = 0
    while n>0:
        if n & 1:
            count+=1
        n = n >> 1
    return count

number = 9
num1 = 50
set_bits = count_set_bits_rightshifting(number)
print(set_bits)
print(count_set_bits_rightshifting(num1))

#using kernighan's algo
def count_set_bits_kernighan(n):
    count = 0
    while n>0:
        n = n & (n-1)
        count +=1
    return count

number = 50
print("using kernighan algo to find set bits:")
print(count_set_bits_kernighan(number))
