def subarraySum(nums,k):
    # All prefixes we have seen so far. So, if we are total - k elements off, this denotes how many ways
    # We can cut off that difference to create our contiguous subarray
    prefixes = {0: 1}
    total = 0
    amount = 0
    for num in nums:
        # Keep a running count (THIS IS THE PREFIX WE CAN TAKE AWAY LATER
        total += num
        # Our heat check step, how far off are we? Additionally, if we have seen a way we can chop off some
        # elements prior that will reduce that distance to 0, get all those ways. As a result, when we
        # get the holder[total-k] amount of ways to chop off the dead weight, we are guaranteed to
        # have holder[total-k] ways to form a contiguous subarray of weight k
        if total - k in prefixes.keys():
            amount += prefixes[total - k]

        # If this is a prefix we haven't seen before, add it to the prefixes
        if total not in prefixes.keys():
            prefixes[total] = 0

        # increment the total number of prefixes of this size we have seen
        prefixes[total] += 1
    return amount

"""

Idea here:

So, we can't do the two pointers and sliding window because elements can be negative, bummer.

However, we can do this idea of prefix chopping that will allow us to get a very similar result.
As we iterate over the array, if we sum up everything we've gotten to that point, we have a prefix
    (This means that all values up to that point have a certain value)

If we were able to get a prefix prior that evaluated to our total - k, that means there are that many ways
we can chop off prefixes to get contiguous subarrays
"""


print(subarraySum([1,3,4,-7,2,-2,4,2,-6],0))