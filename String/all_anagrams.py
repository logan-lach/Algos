from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    # Can 100 percent do this in O(p + s) time

    if len(s) < len(p):
        return 0

    hold = dict()

    for x in p:
        if x in hold.keys():
            hold[x] += 1
        else:
            hold[x] = 1

    check = dict()

    for x in range(len(p)):
        if s[x] in check.keys():
            check[s[x]] += 1
        else:
            check[s[x]] = 1

    total = []

    if check == hold:
        total.append(0)

    for i in range(len(p), len(s)):

        spot = s[i - len(p)]

        if spot in check.keys():
            check[spot] -= 1

            if check[spot] == 0:
                del check[spot]

        spot = s[i]

        if spot in check.keys():
            check[spot] += 1
        else:
            check[spot] = 1

        if check == hold:
            total.append(i - (len(p) - 1))

    return total

