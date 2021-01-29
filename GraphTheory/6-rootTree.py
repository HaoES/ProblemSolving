class TreeNode:
    def __init__(self, id, parent, child):
        self.id = id
        self.parent = parent
        self.child = []


g = {0: set([1, 2, 5]),  # adjacency list undirected
     1: set([0]),
     2: set([0, 3]),
     3: set([2]),
     4: set([5]),
     5: set([0, 4, 6]),
     6: set([5])}


def rootTree(g, rootId=0):
    root = TreeNode(rootId, None, [])
    return buildTree(g, root, None)

# build the tree recursively depth first


def buildTree(g, node, parent):
    for childId in g[node.id]:
        # avoid addind an edge pointing back to the parent
        if parent != None and childId == parent.id:
            continue
        child = TreeNode(childId, node, [])
        node.child.append(child)
        buildTree(g, child, node)
    return node


rooted = rootTree(g)
