
weights = [5,3,2,4,6,4,1,8,3,5]
values = [5,2,8,1,1,5,0,3,2,4]
C = 15
n = 10
prev = {i: [-1 for i in range(n)] for i in range(C + 1)}

def knapsack(C,n):
    if n-1 == -1 or C == 0:
        return 0

    if weights[n-1] > C:
        return knapsack(C, n-1)

    t1 = prev[C][n-1] if prev[C][n-1] != -1 else knapsack(C, n-1)
    prev[C][n-1] = t1

    hold = weights[n-1]
    t2 = prev[C - hold][n-1] if prev[C - hold][n-1] != -1 else values[n-1] + knapsack(C - hold, n - 1)
    prev[C - hold][n-1] = t2

    return max(t1,t2)

print(knapsack(C,n))

