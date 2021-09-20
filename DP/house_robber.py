
"""
Was super close with this one. Had the right idea to check back one house before and grab the max we could get
when adding the current house plus ones before and then storing it. Just couldn't figure out how to do the check
behind in linear time
"""

def initial_solution(A):

    previous = [0,0]
    maximum = 0
    for i in range(len(A)):

        start = 0
        curr_max = 0
        while start < i+1:
            curr_max = max(curr_max, previous[start] + A[i])
        previous.append(curr_max)
        maximum = max(maximum, curr_max)
    return maximum


def optimal_solution(A):

    previous = [0,0]
    maximum = 0
    for i in range(len(A)):
        # Maximum of robbing this house and the loot that comes from maximum sequence behind, or just skipping house outright
        maximum = max(maximum[i] + A[i], maximum[i+1])
        previous.append(maximum)
    return maximum




