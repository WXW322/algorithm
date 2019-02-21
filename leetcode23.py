# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None






class MinHeap(object):

    def __init__(self,datas):
        self.data = datas  # 创建堆
        self.count = len(self.data)  # 元素数量

    #def __init__(self, arr):
    #    self.data = copy.copy(arr)
    #    self.count = len(self.data)
    #    i = self.count / 2
    #    while i >= 1:
    #        self.shiftDown(i)
    #        i -= 1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self, item):
        # 插入元素入堆
        #print(self.count)
        self.data.append(item)
        self.count += 1
        self.shiftup(self.count)

    def shiftup(self, count):
        # 将插入的元素放到合适位置，保持最大堆
        while count > 1 and int(count/2)-1 >= 0 and self.data[int(count/2)-1].val > self.data[int(count)-1].val and int(count)-1 >= 0:
            #print('enter')
            self.data[int((count/2))-1], self.data[int(count)-1] = self.data[int(count)-1], self.data[int((count/2))-1]
            count /= 2

    def extractMax(self):
        # 出堆
        if self.count > 0:
            ret = self.data[0]
            self.data[0], self.data[self.count-1] = self.data[self.count-1], self.data[0]
            self.data.pop()
            self.count -= 1
            self.shiftDown(1)
            return ret

    def shiftDown(self, count):
        # 将堆的索引位置元素向下移动到合适位置，保持最大堆
        while 2 * count <= self.count :
            # 证明有孩子
            j = 2 * count
            if j + 1 <= self.count:
                # 证明有右孩子
                if self.data[j].val < self.data[j-1].val:
                    j += 1
            if self.data[count-1].val <= self.data[j-1].val:
                # 堆的索引位置已经大于两个孩子节点，不需要交换了
                break
            self.data[count-1], self.data[j-1] = self.data[j-1], self.data[count-1]
            count = j

    def show(self):
        for data in self.data:
            print(data.val,end=',')
        print("")

class Solution:
    def get_listnode(self,datas):
        t_head = None
        t_pre = None
        for data in datas:
            t_n = ListNode(data)
            if t_head is None:
                t_head = t_n
                t_pre = t_n
            else:
                t_pre.next = t_n
                t_pre = t_n
        return t_head

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #t_plists = {}
        heap = MinHeap([])
        for i in range(len(lists)):
            if(lists[i] is None):
                continue
            heap.insert(lists[i])
            #t_plists[i] = lists[i].next

        t_r = []
        while(not heap.isEmpty()):
            #print('s')
            t_idom = heap.extractMax()
            #print(t_idom.val)
            if(t_r == ""):
                t_r.append(t_idom.val)
            else:
                t_r.append(t_idom.val)
            #t_key = t_idom[0]
            #t_pre = t_plists[t_key]
            if(t_idom.next != None):
                t_p = t_idom.next
                heap.insert(t_p)
            #heap.show()
            #print('ee')
        return self.get_listnode(t_r)


def get_list(datas):
    t_head = None
    t_pre = None
    for data in datas:
        t_n = ListNode(data)
        if(t_head == None):
            t_head = t_n
            t_pre = t_n
        else:
            t_pre.next = t_n
            t_pre = t_n
    return t_head

def print_L(list):
    t_p = list
    while(not t_p is None):
        print(t_p.val,end='->')
        t_p = t_p.next
t_lists = []
t_s = get_list([-1,1])
t_sone = get_list([-3,1,4])
t_stwo = get_list([-2,-1,0,2])
t_lists.append(t_s)
t_lists.append(t_sone)
t_lists.append(t_stwo)
ss = Solution()
print_L(ss.mergeKLists([t_s,t_sone,t_stwo]))