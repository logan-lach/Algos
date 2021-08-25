def minSteps(self, s: str, t: str) -> int:
    letters = dict()

    for i in s:
        if i in letters.keys():
            letters[i] += 1
        else:
            letters[i] = 1

    for i in t:
        if i in letters.keys():
            letters[i] -= 1

    return sum([abs(x) for x in letters.values()])