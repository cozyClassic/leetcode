class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = Z = ListNode(None)
        result.next = head

        while head and head.next:
            # save pointer for C
            B = head.next
            C = B.next
            # (Z) -> A -> B => (Z) -> B -> A
            Z.next, B.next, head.next = B, head, C

            # move pointer (Z) -> B -> A => (A>Z) -> (C->A)
            Z, head = head, C

        return result.next