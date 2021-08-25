from typing import List


def numberOfWeeks(A: List[int]) -> int:
    A = sorted(A)

    s_ptr = 0
    e_ptr = len(A) - 1

    count = 0
    while s_ptr < e_ptr:
        if count % 2 == 0:
            A[e_ptr] -= 1
            count += 1
        else:
            A[s_ptr] -= 1
            count += 1

        if A[s_ptr] == 0:
            s_ptr += 1
        elif A[e_ptr] == 0:
            e_ptr -= 1

    return count + 1

print( numberOfWeeks([9,3,6,8,2,1]))