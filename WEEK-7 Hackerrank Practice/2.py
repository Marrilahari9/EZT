""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
""

class Solution:
    def iterate(self, head) -> None:
        if head is None:
            return [None, None]
        first = head
        if first.child and first.next is None:
            temp = first.child
            first.child = None
            m, n = self.iterate(temp)
            first.next = m
            m.prev = first
            itr = first
            while itr.next:
                itr = itr.next
            return first, itr

        itr = first
        while itr.next:
            if itr.child:
                temp = itr.next
                temp.prev = None
                itr.next = None
                child = itr.child
                itr.child = None
                j, k = self.iterate(child)
                itr.next = j
                j.prev = itr
                temp.prev = k
                k.next = temp
            else:
                itr = itr.next
        
        if itr.child:
            temp = itr.child
            itr.child = None
            m, n = self.iterate(temp)
            itr.next = m
            m.prev = itr
        
        while itr.next:
            itr = itr.next

        return [first, itr]

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = self.iterate(head)
        return res[0]