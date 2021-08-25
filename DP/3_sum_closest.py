import math
def three_sum_closest(A, target):
    curr_max = math.inf

    for i in range(len(A) - 2):
        small = i + 1
        end = len(A) - 1

        while small < end:

            value = A[i] + A[small] + A[end]

            if value < target:
                small += 1
            else:
                end -= 1

            curr_max = min(curr_max, value, key=lambda x: abs(target - x))
    return curr_max

print(three_sum_closest([-1,2,1,-4],
1))