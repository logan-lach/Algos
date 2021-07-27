# This one is maximum subarray

def buy_sell_stock_bruteforce(A):

    max_score = 0

    for i in range(len(A)):
        for j in range(i + 1,len(A)):
            max_score = A[j] - A[i] if A[j] - A[i] > max_score else max_score
    return max_score

