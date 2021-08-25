seen = dict()


def recursion(s):
    if len(s) == 0:
        return 0

    if len(s) == 1:
        return 1

    if s[0] == '0':
        return 0

    if s in seen.keys():
        return seen[s]

    jump = 0
    if s[0] == '1' or (s[0] == '2' and 1 < len(s) and int(s[1]) <= 6):
        jump = recursion(s[2:])
    step = recursion(s[1:])
    seen[s] = jump + step
    return step + jump


print(recursion("12"))