class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        l1=[]
        curr=list1
        while curr!=None:
            l.append(curr.val)
            curr=curr.next
        curr=list2
        while curr!=None:
            l1.append(curr.val)
            curr=curr.next
        l2=l1+l
        l2=sorted(l2)
        newnode=ListNode(0)
        curr=newnode
        print(l2)
        for i in l2:
            curr.next=ListNode(i)
            curr=curr.next
        return newnode.next
