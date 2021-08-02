

def shortest(A, seq):

    start = 0

    curr_occupied = seq.copy()

    length = len(A) + 1

    for i in range(len(A)):
        if A[i] in curr_occupied:
            curr_occupied.remove(A[i])

        if len(curr_occupied) == 0:
            length = min(length, i - start + 1)
            while start < len(A) and start < i and A[start] not in seq:
                start += 1
            curr_occupied = seq - {A[start], A[i]}
