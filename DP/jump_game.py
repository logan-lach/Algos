def jump_game(A):
    reach = A[0]
    for i in range(1,len(A)):
        if i > reach:
            return False
        reach = max(reach, i + A[i])
        if reach >= len(A) - 1:
            return True


# Assuming a guarantee to reach the end
def jump_game_min_jumps(A):

    jumps = 1
    reach = A[0]
    curr_max = 0
    count = 0
    while reach < len(A) - 1 and count < len(A):
        count += 1
        curr_max = max(curr_max, count + A[count])
        if count == reach:
            reach = curr_max
            jumps += 1
            curr_max = 0
    return jumps

print(jump_game_min_jumps([2,3,1,1,4]))



