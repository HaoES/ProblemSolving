# sums up leaf node values in a tree
# the function is called by: leafsum(root)
tree = {0: set([1, 4]),  # adjacency list
        1: set([2]),
        2: None,
        3: None,
        4: set([3, 5]),
        5: None}


def leafSum(node):
    # handle empty tree case
    if node == None:
        return 0
    if isLeaf(node):
        return node
    total = 0
    for child in tree[node]:
        total += leafSum(child)
    return total


def isLeaf(node):
    return tree[node] == None


print(leafSum(0))
