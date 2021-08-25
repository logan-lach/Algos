def find_non_duplicate(A):
    xor_val = 0

    for i in A:
        xor_val ^= i
    return xor_val

print(find_non_duplicate([2,1,1,2,3,4,4,5,6,7,7,6,5]))