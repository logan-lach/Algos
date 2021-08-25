import math
def tower_problem(listeners, towers):

    # Not assuming towers and listeners are sorted, sort them out

    listeners = sorted(listeners)
    towers = sorted(towers)

    tower_ptr = 0
    listener_ptr = 0

    distance = math.inf

    while listener_ptr < len(listeners):

        # Constant O(n) time where n denotes length of tower list
        while tower_ptr < len(towers)-1 and listeners[listener_ptr] > towers[tower_ptr]:
            tower_ptr += 1

        if tower_ptr == 0:
            distance = min(distance, towers[tower_ptr] - listeners[listener_ptr])
        else:
            distance = min(distance, abs(towers[tower_ptr] - listeners[listener_ptr]), abs(towers[tower_ptr - 1] - listeners[listener_ptr]))

        listener_ptr += 1
    return distance

print(tower_problem([1,5,11,20], [4,8,15]))


