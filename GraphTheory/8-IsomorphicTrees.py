class TreeNode:
    def __init__(self, id, parent, child):
        self.id = id
        self.parent = parent
        self.child = []


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
# returns whether two trees are isomorphic
# parameters are tree1 and tree2 are undirected trees as adjacency lists.


tree1 = {0: set([1]),  # adjacency list undirected
         1: set([2]),
         2: set([1, 3, 4, 5]),
         3: set([2]),
         4: set([2]),
         5: set([2]),
         }
tree2 = {0: set([1]),  # adjacency list undirected
         1: set([0, 2, 4]),
         2: set([1]),
         3: set([4]),
         4: set([1, 3, 5]),
         5: set([4]),
         }


def isIsomorphic(tree1, tree2):
    tree1_centers = treeCenters(tree1)
    tree2_centers = treeCenters(tree2)

    tree1_rooted = rootTree(tree1, tree1_centers[0])
    tree1_encoded = encode(tree1_rooted)

    for center in tree2_centers:
        tree2_rooted = rootTree(tree2, center)
        tree2_encoded = encode(tree2_rooted)
        # two trees are isomorphic if their encoded rooted forms are equal
        if tree1_encoded == tree2_encoded:
            return True
        return False


def encode(node):
    if node == None:
        return ''
    labels = []
    for child in node.child:
        labels.append(encode(child))

    labels.sort()
    result = ""
    for label in labels:
        result += str(label)
    return '(' + result + ')'


print(isIsomorphic(tree1, tree2))
