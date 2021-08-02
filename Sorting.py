def binary_search(A, target):

    start = 0
    end = len(A) -1

    while start < end:
        mid = int((start + end) / 2)

        if A[mid] < target:
            if mid == start:
                end = mid
            else:
                start = mid

        elif A[mid] > target:
            if mid == end:
                start = mid
            else:
                end = mid

        else:
            return mid

    return -1

print(binary_search([1,4,7,11,15], 5))