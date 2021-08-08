from typing import List


def isNStraightHand_optimalimplementation(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    # Initial Check, if it isn't even divisible don't bother doing the rest
    holder = dict()

    for i in hand:
        if i in holder.keys():
            holder[i] += 1
        else:
            holder[i] = 1

    h = sorted(holder.keys())
    for key in h:
        if holder[key] > 0:
            for i in range(key+1, key+groupSize):
                if i not in holder.keys() or holder[i] != holder[key]:
                    return False
                else:
                    holder[i] -= holder[key]

    return True


def isNStraightHand_myimplementation(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

        # Initial Check, if it isn't even divisible don't bother doing the rest
    holder = dict()

    for i in hand:
        if i in holder.keys():
            holder[i] += 1
        else:
            holder[i] = 1

    available = sorted(holder.keys())

    while len(available) != 0:

        for i in range(1, groupSize):
            if i >= len(available) or available[i] - available[i - 1] != 1:
                return False

        g = groupSize
        i = 0
        while i < g:
            holder[available[i]] -= 1
            if holder[available[i]] == 0:
                del available[i]
                g -= 1
            else:
                i += 1

    return True

print(isNStraightHand_optimalimplementation([1,2,3,3,4,4,5,6],
4))

