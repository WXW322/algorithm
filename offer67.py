
class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None


def buildtree(values):
    t_head = None
    t_trees = {}
    T_len = len(values)
    for i in range(T_len):
        t_node = Node(values[i])
        t_trees[i+1] = t_node
        if t_head == None:
            t_head = t_node
        else:            
            t_p = int((i + 1) / 2)
            t_lo = (i + 1) % 2
            p = t_trees[t_p]
            if t_lo == 0:
                p.left = t_node
            else:
                p.right = t_node
            t_node.parent = p
    return t_head
            
def get_n(value, h):
    t_n = h
    while(1):
        if t_n == None:
            break
        if t_n.val == value:
            return t_n
        elif value < t_n.val:
            t_n = t_n.left
        else:
            t_n = t_n.right
    return t_n


def get_next(node):
    if node == None:
        return None
    t_next = None
    t_lo = 0
    if node.right != None:
        t_n = node.right
        while(t_n.left != None):
            t_n = t_n.left
        t_next = t_n
    if t_next == None:
        t_c = node
        t_n = node.parent
        while(t_n != None and t_c == t_n.right):
            t_c = t_n
            t_n = t_n.parent
        if t_n != None:
            t_next = t_n
    return t_next


h = buildtree([5])
p = get_n(3, h)
t_c = get_next(p)
if t_c == None:
    print('n')
else:
    print(t_c.val)
