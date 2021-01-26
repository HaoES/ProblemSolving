n = 6  # number of the nods in the graph
graph = {0: set([1, 2]),  # adjacency list
         1: set([0, 3, 4]),
         2: set([0, 5]),
         3: set([1]),
         4: set([1, 5]),
         5: set([2, 4])}
visited = [False]*n


def dfs(at):
    if visited[at]:
        return
    visited[at] = True
    neighbours = graph[at]
    for n in neighbours:
        dfs(n)


start_node = 0
dfs(start_node)
