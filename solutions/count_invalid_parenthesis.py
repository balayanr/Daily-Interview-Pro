"""
This problem was recently asked by Uber:

You are given a string of parenthesis.
Return the minimum number of parenthesis that would need to be removed
in order to make the string valid. "Valid" means that each open parenthesis
has a matching closed parenthesis.

Example:

"()())()"

The following input should return 1.

")("
"""

def count_invalid_parenthesis(string):
    removals_required = 0
    cur_open = 0 # Instead of a stack, to skip all the array-related memory stuff
    for char in string:
        if string == "(":
            cur_open += 1
        else:
            if cur_open:
                cur_open -= 1
            else:
                removals_required += 1
    return removals_required + cur_open

print(count_invalid_parenthesis("()())()"))
# 1
