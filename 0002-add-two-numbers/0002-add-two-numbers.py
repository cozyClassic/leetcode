class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cursor = ListNode(0)
        overflow = 0

        while l1 or l2 or overflow:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            overflow, val = divmod(val+overflow, 10)
            cursor.next = ListNode(val)
            cursor = cursor.next

        return head.next