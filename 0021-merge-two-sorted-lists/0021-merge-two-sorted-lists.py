# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # head가 비어있는 노드를 하나 만든다.
        new_node = ListNode(-101)
        now = new_node

        # 작은 값부터 잇는다.
        while l1 and l2:
            if l1.val > l2.val :
                now.next = ListNode(l2.val)
                l2 = l2.next

            else :
                now.next = ListNode(l1.val)
                l1 = l1.next
            now = now.next
        
        while l1:
            now.next = ListNode(l1.val)
            l1 = l1.next
            now = now.next
        
        while l2:
            now.next = ListNode(l2.val)
            l2 = l2.next
            now = now.next

        return new_node.next