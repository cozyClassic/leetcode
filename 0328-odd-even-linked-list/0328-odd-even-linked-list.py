class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = oddList = head
        even = evenList = head.next

        while odd and even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = even.next.next
            even = even.next
        
        odd.next = evenList

        return oddList
