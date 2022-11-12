# I want to come back to this problem and 
# study the way to walk through the list

def longestCPrefix(strs):

    # base cases
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    # making the prefix equal to the first string in list
    our_prefix = strs[0]
    # setting the length equal to that prefix
    prefix_length = len(our_prefix)
    # for loop to look at the remaining elements in our
    # list of strings. We are staring at index 1 to the end
    for element in strs[1:]:
        # while prefix at index 0 is of different length
        # to the next string in the list
        while our_prefix != element[0:prefix_length]:
            # we subtract the ending off of the our orignal prefix
            our_prefix = our_prefix[0:prefix_length-1]
            # we subtract 1 from the length of the original prefix
            prefix_length -= 1
            # if the prefix length gets to zero return the empty list
            if prefix_length == 0:

                return ""
    # if it is to this point there is a positive length return the common 
    # prefixes
    return our_prefix

