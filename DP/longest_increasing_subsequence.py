def longest_increasing_subsequence(A):

    maxes = [1] * len(A)
    maximum = 0
    for i in range(len(A)):
        curr_max = 0
        for j in range(i):
            if A[j] < A[i]:
                curr_max = max(curr_max, maxes[j])
        maxes[i] = curr_max
        maximum = max(curr_max, maximum)

    return maximum
