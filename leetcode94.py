# Definition for a binary tree node.
import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_tree(datas):
    q = queue.Queue()
    if len(datas) == 0:
        return None
    data = datas[0]
    root = TreeNode(data)
    q.put(root)
    i = 0
    while(i < len(datas)):
        node = q.get()
        t_left = None if i+1 >= len(datas) else datas[i+1]
        t_right = None if i+2 >= len(datas) else datas[i+2]
        if t_left != None:
            node_l = TreeNode(t_left)
            node.left = node_l
            q.put(node_l)
        if t_right != None:
            node_r = TreeNode(t_right)
            node.right = node_r
            q.put(node_r)
        i = i + 2
    while(not q.empty()):
        q.get()
    ss = Solution()
    s_r = ss.inorderTraversal(root)
    print(s_r)


        


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.list = []
        if root != None:
            self.reout(root)
        return self.list


    def reout(self, node):
        if node.left != None:
            self.reout(node.left)
        self.list.append(node.val)
        if node.right != None:
            self.reout(node.right)
get_tree([1,None,2,3])
