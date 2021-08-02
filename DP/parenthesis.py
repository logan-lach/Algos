def parenthesis(n, o, c):
    if n == 1:
        return [")"]

    if o == c:
        left = ["(" + x for x in parenthesis(n-1,o-1,c)]
        return left

    elif o == 0:
        right = [")" + x for x in parenthesis(n-1,o,c-1)]
        return right

    else:
        left = ["(" + x for x in parenthesis(n-1,o-1,c)]
        right = [")" + x for x in parenthesis(n-1,o,c-1)]
        return left+right


print(parenthesis(6,3,3))