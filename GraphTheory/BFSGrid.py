import queue
# Global Variables
R, C = 4, 5  # R = number of rows, C = number of columns
m = [['S', '.', '.', '.', '.'],
     ['.', '#', '#', '#', '.'],
     ['.', '#', '#', '.', '.'],
     ['#', '#', '#', 'E', '#'],
     ]  # Input character matrix of size R x C

# empty row queue (rq) and column queue (cq)
rq = queue.Queue()
cq = queue.Queue()
sr, sc = 0, 0  # 'S' symbol position, row and columns values

# Variables used to track the number of steps taken
move_count = 0
nodes_left_in_layer = 1
nodes_in_next_layer = 0

# Variables used to track whether the 'E' character ever gets
# reached during the BFS.
reached_end = False

# R x C matrix of false values used to track whether the node at
# position (i,j) has been visited.
visited = [[False]*5, [False]*5, [False]*5, [False]*5]

# North, South, East, West direction vectors.
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def solve():
    global nodes_left_in_layer
    global move_count
    global nodes_in_next_layer
    global reached_end
    rq.put(sr)
    cq.put(sc)
    visited[sr][sc] = True
    while not rq.empty():
        r = rq.get()
        c = cq.get()
        if m[r][c] == 'E':
            reached_end = True
            break
        explore_neighbours(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
    if reached_end:
        return move_count
    return -1


def explore_neighbours(r, c):
    global nodes_in_next_layer
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

    # skip out of bounds locations
        if rr < 0 or cc < 0:
            continue
        if rr >= R or cc >= C:
            continue
    # skip visited locations and blocked cells
        if visited[rr][cc]:
            continue
        if m[rr][cc] == '#':
            continue

        rq.put(rr)
        cq.put(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1


print(solve())
