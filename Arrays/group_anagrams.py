def groupAnagrams(strs):
    seen_strings = set()
    holder = dict()
    for i in strs:
        temp = ''.join(sorted(i))
        if temp in seen_strings:
            holder[temp] += [i]
        else:
            holder[temp] = [i]
            seen_strings.add(temp)
    return holder.values

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

'''
Intuition here:

1.) For every single word, we want to see if it can be spelled the same
    - We can check if two words are being spelled the same if they are the same in sorted order
    - Originally wanted to do this with a dictionary, but dictionaries are not hashable.
        - String are hashable, giving us O(1) runtime
    - 
'''