n = 6  # number of the nods in the graph
graph = {0: set([1, 2]),
         1: set([0, 3, 4]),
         2: set([0, 5]),
         3: set([1]),
         4: set([1, 5]),
         5: set([2, 4])}
count = 0  # number of connected components
components = [0]*n
visited = [False]*n


def findComponents():
    global count
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return (count, components)


def dfs(at):
    visited[at] = True
    components[at] = count
    for neighbour in graph[at]:
        if not visited[neighbour]:
            dfs(neighbour)


print(findComponents())
