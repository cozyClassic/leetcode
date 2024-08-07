class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = Z = ListNode(None)
        result.next = A = head

        while A and A.next:
            # save pointer for C
            B = A.next
            C = B.next
            # (Z) -> A -> B => (Z) -> B -> A
            Z.next, B.next, A.next = B, A, C

            # move pointer (Z) -> B -> A => (A>Z) -> (C->A)
            Z, A = A, C

        return result.next