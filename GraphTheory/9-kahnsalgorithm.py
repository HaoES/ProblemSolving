import queue
# 'g' is a directed acyclic graph as an adjancency list.
graph = {0: set([2, 6, 3]),  # adjacency list undirected
         1: set([4]),
         2: set([6]),
         3: set([4, 1]),
         4: set([5, 8]),
         5: None,
         6: set([7, 11]),
         7: set([12]),
         8: None,
         9: set([10]),
         10: set([6]),
         11: set([12]),
         12: None,
         13: None}


def findTopologicalOrdering(g):
    n = len(graph)
    in_degree = [0]*n
    for i in range(n):
        if g[i] != None:
            for to in g[i]:
                in_degree[to] = in_degree[to] + 1

# 'q' always contains the set nodes with no incoming edges.
    q = queue.Queue()
    for i in range(n):
        if in_degree[i] == 0:
            q.put(i)

    index = 0
    order = [0]*n
    while not q.empty():
        at = q.get()
        order[index] = at
        index += 1
        if g[at] != None:
            for to in g[at]:
                in_degree[to] = in_degree[to] - 1
                if in_degree[to] == 0:
                    q.put(to)
    if index != n:
        return None  # Graph contains a cycle
    return order


print(findTopologicalOrdering(graph))
