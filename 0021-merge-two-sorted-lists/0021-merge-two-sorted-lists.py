class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l2, l1 = l1, l2
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1