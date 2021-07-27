'''
This is the divide and conquer solution to our problem
'''


'''
So our main idea is as follows. Divide and conquer focuses on 
SPLITTING OUR ARRAY IN TWO ALONG THE MIDDLE.

So in our array, we split into our left and right half of the array.
WE FIND THE LARGEST SUBARRAY THAT STARTS AT THE MIDDLE OF OUR ARRAY.

With this, we form a subarray starting at the middle going to the left,
and then a subarray starting at the middle going to the right.

We then have three options. Is the left array, right array, OR THE MERGE
OF THE TWO (As they are both focused on the middle) The largest subarray.
We then return the max of these values.




Had this not been a recursive solution, there would be obvious holes. However,
on every split, we run a RECURSIVE CALL in order to find the max subarray at an even 
smaller level.

So to finish, our main idea here is dividing our array up to FIND THE ELEMENT THAT IS
CONTAINED/THE CENTER OF OUR LARGEST SUBARRAY. From there, we branch left on that point,
we branch right from that point, and see if we have our largest there
'''
def divide_and_conquer(A,l,r):


    '''
    base case:

    if on our splits, we finally get down to only one element, return it.
    '''
    if(r == 1):
        return A[l]

    else:

        '''
        Split our list into 2.
        
        Our left hand max is our centerpoint, and the 
        sum is currently our center spot
        
        we're gonna add out and find the max contiguous sum, that includes our centerpoint.
        '''
        c = (int)((1 + r)/2)
        lhmax = A[c]
        lhsum = 0
        for i in range(c,l-1, -1):
            lhsum = lhsum + A[i]
            if lhsum > lhmax:
                lhmax = lhsum

        '''
        the same exact process here. We are going to find the greatest contiguous sum
        going from the right here. 
        '''
        rhmax = A[c+1]
        rhsum = 0
        for j in range(c+1, r+1):
            rhsum = rhsum + A[j]
            if rhsum > rhmax:
                rhmax = rhsum

        '''
        cmax is the combination fo the left and right. We know that we can do this because
        both lmax and rmax include our center spot. So the cmax is a perfectly valid 
        contiguous sum 
        
        We will also be guaranteed to use cmax here. The goal of each recursive call
        is to find the greatest l/r values that include this center point. 
        '''
        cmax = lhmax + rhmax
        lmax = divide_and_conquer(A, l, c)
        rmax = divide_and_conquer(A,c+1,r)
        return max([lmax,rmax,cmax])


print(divide_and_conquer([1,5,-4,6,3,-9,1,-15], 0,7))