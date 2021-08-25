import math
def max_product(A):
    minSuffixProd = 1
    maxSuffixProd = 1
    maxSoFar = -math.inf
    for x in A:
        prev_max = maxSuffixProd
        maxSuffixProd = max(maxSuffixProd * x, x, minSuffixProd * x)
        minSuffixProd = min(minSuffixProd * x, x, prev_max * x)
        maxSoFar = max(maxSuffixProd, maxSoFar)
    return maxSoFar

print(max_product([2,3,-2,4]))
