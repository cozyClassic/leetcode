# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        word = ""
        while head:
            word += str(head.val)
            head = head.next

        if len(word)%2 == 0:
            return word[:len(word)//2] == word[len(word)//2:][::-1]
        return word[:len(word)//2] == word[len(word)//2+1:][::-1]
