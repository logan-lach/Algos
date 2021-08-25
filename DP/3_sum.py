def three_sum(A):
    A = sorted(A)
    s = 0
    e = len(A) - 1

    results = []



    for i in range(len(A)-2):
        small = i + 1
        end = len(A) - 1
        while small < end:
            value = A[i] + A[small] + A[end]

            if value > 0:
                end -= 1
            elif value < 0:
                small += 1
            else:
                if [A[i], A[small], A[end]] not in results:
                    results.append([A[i], A[small], A[end]])
                small += 1
    return results



print(three_sum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))