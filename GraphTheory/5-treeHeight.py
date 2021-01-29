# the height of a tree is the number of edges from the root to the lowest leaf.
tree = {0: set([1, 4]),  # adjacency list
        1: set([2]),
        2: set([7]),
        3: None,
        4: set([3, 5]),
        5: None,
        7: None}


def treeHeight(node):
    # empty tree case
    if node == None:
        return -1

    # identify leaf nodes and return zero
    if tree[node] == None:
        return 0
    return max(map(treeHeight, tree[node])) + 1


print(treeHeight(0))
