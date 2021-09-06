def subsets(A):

    if len(A) == 0:
        return [[]]

    value = A[-1]
    A.pop()
    prev_values = subsets(A)
    hold = prev_values[:]

    for i in range(len(prev_values)):
        hold.append(prev_values[i] + [value])

    return hold

print(subsets([1,2,3]))