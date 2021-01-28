import queue
n = 6  # number of the nods in the graph
graph = {0: set([1, 2]),  # adjacency list
         1: set([0, 3, 4]),
         2: set([0, 5]),
         3: set([1]),
         4: set([1, 5]),
         5: set([2, 4])}
# s = start node, e = end node, and 0 <= e,s <= n


def bfs(s, e):
    # do a BFS starting at node s
    prev = solve(s)

    # return reconstructed path from s -> e
    return reconstructPath(s, e, prev)

# a function that return a list of the parents of all the nodes of the graph


def solve(s):
    q = queue.Queue()
    q.put(s)

    visited = [False]*n
    visited[s] = True

    prev = [None]*n
    while not q.empty():
        node = q.get()
        neighbours = graph[node]

        for neighbour in neighbours:
            if not visited[neighbour]:
                q.put(neighbour)
                visited[neighbour] = True
                prev[neighbour] = node
    return prev

# a function that returns the shortest path between the source node and the end node


def reconstructPath(s, e, prev):
    # Reconstruct path going backwards from e
    path = [e]

    def parent(e):
        while prev[e] != None:
            yield prev[e]
            e = prev[e]
    for at in parent(e):
        path.append(at)

    path.reverse()

    # If s and e are connected return the path
    if s == path[0]:
        return path

    return []


print(bfs(0, 4))
