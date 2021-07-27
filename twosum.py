def twosum_bruteforce(A, target):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] + A[j] == target:
                return [A[i], A[j]]


def twosum_linear(A,target):
    lv = {}
    for i in range(len(A)):
        var = target-A[i]
        if var in lv.keys():
            return [i, lv[var]]
        else:
            lv[A[i]] = i
    return False