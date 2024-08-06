from collections import deque
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Q = deque()
        while head:
            Q.append(head.val)
            head = head.next

        while Q:
            try:
                r = Q.pop()
                l = Q.popleft()
                if r != l:
                    return False
            except:
                break
        return True
