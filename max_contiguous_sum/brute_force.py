'''
The most primitve method we have studied so far, the brute force approach

This one is a less clever version of kadanes, all we do is iterate through every starting
point, and see if the subarray from the start, to the end is the largest
'''

def brute_force(A):

    '''

    :param A: list passing into our function holding our values
    :return: the largest contiguous subarray
    '''

    #max_sum and max_list are constant, cannot be modifed by loop iteration. Store value and list of largest subarray
    max_sum = A[0]
    max_list = [A[0]]
    for i in range(len(A)):
        '''
        Starting at 0, have our two sums and lists ready to store all values
        '''
        curr = A[i]
        curr_list = [A[i]]

        '''
        Starting one ahead of curr and curr_list, Add all the possible values to our list
        '''
        for j in range(i + 1, len(A)):
            curr += A[j]
            curr_list += [A[j]]

            '''
            Check everytime and see if it worked out. Did our addition yield the highest subarray?
            '''
            if curr > max_sum:
                max_sum = curr
                max_list = curr_list[:]

    return max_list


print(brute_force([20,-2,0,-4,9,2,-10,-15]))