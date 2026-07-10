# Problem : Delete the Middle Node of a Linked List
# Topic : Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        # Find length
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        mid = length // 2
        # Find mid - 1
        temp = head
        for i in range(mid - 1):
            temp = temp.next
        # delete mid
        temp.next = temp.next.next
        return head
