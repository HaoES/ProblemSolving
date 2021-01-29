
g = {0: set([1, 2, 5]),  # adjacency list undirected
     1: set([0]),
     2: set([0, 3]),
     3: set([2]),
     4: set([5]),
     5: set([0, 4, 6]),
     6: set([5])}


def treeCenters(g):
    n = len(g)
    degree = [0]*n
    leaves = []
    for i in range(n):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)
            degree[i] == 0
    count = len(leaves)
    while count < n:
        new_leaves = []
        for leaf in leaves:
            for neighbor in g[leaf]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    new_leaves.append(neighbor)
            degree[leaf] = 0
        count += len(new_leaves)
        leaves = new_leaves
    return leaves


print(treeCenters(g))
