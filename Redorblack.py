from collections import deque
import sys
class node:
    def __init__(self,leaf,color,parent,value):
        self.left = leaf
        self.right = leaf
        self.color = color
        self.p = parent
        self.value = value

class tree:
    def __init__(self):
       self.leaf = node(None,'black',None,0)
       self.root = self.leaf

    def lefttraverse(self,x_p):
        x_c = x_p.right
        if(x_c == self.leaf):
            return -1
        x_c.p = x_p.p
        if(x_p.p == self.leaf):
            self.root = x_c
        elif(x_p == x_p.p.left):
            x_p.p.left = x_c
        else:
            x_p.p.right = x_c
        x_p.right = x_c.left
        if(x_c.left != self.leaf):
            x_c.left.p = x_p
        x_p.p = x_c
        x_c.left = x_p
        return 1

    def rightraverse(self,x_p):
        x_c = x_p.left
        if(x_c == self.leaf):
            return -1
        x_c.p = x_p.p
        if(x_p.p == self.leaf):
            self.root = x_c
        elif(x_p == x_p.p.left):
            x_p.p.left = x_c
        else:
            x_p.p.right = x_c
        x_p.left = x_c.right
        if(x_p.left != self.leaf):
            x_p.left.p = x_p
        x_c.right = x_p
        x_p.p = x_c
        return 1

    def re_insert_fixup(self,t):
        while(t.p.color == 'red'):
            if(t.p == t.p.p.left):
                if(t.p.p.right.color == 'red'):
                    t.p.color = 'black'
                    t.p.p.right.color = 'black'
                    t.p.p.color = 'red'
                    t = t.p.p
                else:
                    if (t == t.p.right):
                        t = t.p
                        self.lefttraverse(t)
                    t.p.color = 'black'
                    t.p.p.color = 'red'
                    self.rightraverse(t.p.p)
            else:
                if(t.p.p.left.color == 'red'):
                    t.p.p.left.color = 'black'
                    t.p.color = 'black'
                    t.p.p.color = 'red'
                else:
                    if(t == t.p.left):
                        t = t.p
                        self.rightraverse(t)
                    t.p.color = 'black'
                    t.p.p.color = 'red'
                    self.lefttraverse(t.p.p)
            #self.print_h()
        #print('bb')
        #print("")
        self.root.color = 'black'

    def insert(self,value):
        y = self.leaf
        x = self.root
        while(x != self.leaf):
            y = x
            if(value < x.value):
                x = x.left
            else:
                x = x.right
        t_node = node(self.leaf, 'red', y, value)

        if y == self.leaf:
            self.root = t_node
        elif value < y.value:
            y.left = t_node
        else:
            y.right = t_node
        if(self.root.p == self.leaf):
            print('111')
        else:
            print('222')
        self.re_insert_fixup(t_node)

    def re_transparent(self,unode,vnode):
        if(unode.p == self.leaf):
            self.root = vnode
        elif(unode == unode.p.left):
            unode.p.left = vnode
        else:
            unode.p.right = vnode
        vnode.p = unode.p

    def Re_delete_fixup(self,x):
        while(x != self.root and x.color == 'black'):
            if x == x.p.left:
                w = x.p.right
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.lefttraverse(x.p)
                    w = x.p.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                else:
                    if w.right.color == 'black':
                        w.color = 'red'
                        w.left.color = 'black'
                        self.rightraverse(w)
                        w = x.p.right
                    w.color = w.p.color
                    w.right.color = 'black'
                    w.p.color = 'black'
                    self.lefttraverse(w.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'red':
                    w.color = 'black'
                    x.p.color = 'red'
                    self.rightraverse(x.p)
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.p
                else:
                    if w.left.color == 'black':
                        w.color = 'red'
                        w.right.color = 'black'
                        self.lefttraverse(w)
                        w = x.p.left
                    w.left.color = 'black'
                    w.color = x.p.color
                    x.p.color = 'black'
                    self.rightraverse(x.p)
                    x = self.root
            x.color ='black'

    def get_minimum(self,t_p):
        while(t_p.left != self.leaf):
            t_p = t_p.left
        return t_p

    def delete_node(self,value):
        t_p = self.root
        while(t_p.value != value and t_p != self.leaf):
            if(t_p.value > value):
                t_p = t_p.left
            else:
                t_p = t_p.right
        if(t_p == self.leaf):
            return -1
        t_y = t_p
        t_y_color = t_p.color
        if(t_p.left == self.leaf):
            t_x = t_p.right
            self.re_transparent(t_p,t_p.right)
        elif(t_p.right == self.leaf):
            t_x = t_p.left
            self.re_transparent(t_p,t_p.left)
        else:
            t_y = self.get_minimum(t_p.right)
            t_x = t_y.right
            t_y_color = t_y.color
            if t_y.p == t_p:
                t_x.p = t_y
            else:
                self.re_transparent(t_y,t_y.right)
                t_y.right = t_p.right
                t_p.right.p = t_y
            self.re_transparent(t_p,t_y)
            t_y.left = t_p.left
            t_y.left.p = t_y
            t_y.color = t_p.color
        if t_y_color == 'black':
            self.Re_delete_fixup(t_x)










                


    def print_h(self):
        queue = deque([self.root])
        while(len(queue) > 0):
            idom = queue.popleft()
            print(idom.color,idom.value)
            if(idom.left != self.leaf):
                queue.append(idom.left)
            if(idom.right != self.leaf):
                queue.append(idom.right)



tt = tree()

for a in [11,2,14,1,7,15,5,8,4]:
    tt.insert(a)
tt.print_h()
print("")
tt.delete_node(2)
tt.print_h()







