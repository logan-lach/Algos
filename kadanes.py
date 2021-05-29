def kadanes_1(A):
    total = gcs_value = A[0]
    total_list = [A[0]]
    gcs = [A[0]]

    for i in range(1, len(A)):
        '''
        The opening step. Our combination between everything we seen this far and our new item
        We will check if this contributes something to our growth, we will see shortly
        '''
        t = total + A[i]

        '''
        So, if the combination of everything we have so far is greater than the item itself
        WHAT THIS CAN BE THOUGHT OF IS 'Does the rest of the list weigh this item down?'
        '''
        if t > A[i]:

            '''
            If it doesn't weight it down, then our biggest out of the current items we have seen
            is just the conglomeration of all the items so far.
        
            We will adjust both our current total and total_list to account for this
            '''
            total = t
            total_list += [A[i]]
        else:
            '''
            Else if the rest of the list DOES hold our current item back(more negatives than positives)
            WE NO LONGER HAVE TO CONSIDER THAT PART OF OUR ARRAY AS BEING THE MAX, SO we leave it behind
            in the dust and start anew at our newest member
            '''
            total = A[i]
            total_list = [A[i]]

        '''
        Now, here's the mac daddy step
        
        Throughout it all, we collect our greatest array up to our index i. This array will always 
        grow throughout every iteration, as to gauge if our previous list helps/hurts the cause
        
        Now, this is where A[i] gets gauged. We previously only checked if the rest of the list
        helped/hurt our total. If it didn't, we added A[i] to the list with no questions asked
        
        Now, if adding A[i] HURT THE TOTAL, our variable total will feel it. As such, when we assigned total to our 
        total += A[i] in our previous step, and engage in our comparison now, A[i] will have been revealed 
        to have lowered the total, and therefore the addition to A[i] cannot be greater than the gcs_value 
        
        This also helps differentiate between our i-sized list and the actual max. Just because
        we have added some positive numbers to our total, does that really mean it outweighs the
        negatives you have picked up so far?
        
        The negatives will always be picked up as long as we don't hit a A[i] that is greater than our
        previous list. We have to be mindful of that when considering the real gcs_value
        
        '''
        if total > gcs_value:
            gcs_value = total
            gcs = total_list[:]

    return gcs

print(kadanes_1([1,3,-5,2,3]))