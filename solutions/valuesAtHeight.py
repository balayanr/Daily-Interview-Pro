"""
This problem was recently asked by Amazon:

Given a binary tree, return all values given a certain height h.
"""

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, height):
    def inner_loop(queue, current_height):
        if current_height == height:
            return [item.value for item in queue]
        new_queue = []
        while queue:
            node = queue.pop()
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        return inner_loop(new_queue, current_height + 1)

    return inner_loop([root], 1)

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
# [4, 5, 7]
