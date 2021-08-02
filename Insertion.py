def insertion(A):

    holder = 1
    for i in range(1,len(A)):
        val = A[i]
        while i > 0 and A[i-1] < val:
            A[i] = A[i-1]
            i -= 1
        A[i] = val

    return A

print(insertion([5,2,7,1,3]))