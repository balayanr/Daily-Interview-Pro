"""
This problem was recently asked by Facebook:

You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.
"""
def two_sum(input_list, k):
    # Fill this in.
    as_set = set(input_list)
    for num in as_set:
        if (k - num) in as_set:
            return True
    return False

print(two_sum([4,7,1,-3,2], 5))
# True
