# Problem : Maximum Twin Sum of a Linked List
# Topic : Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        Max = 0
        a = []
        if head is None:
            return 0
        temp = head
        while temp:
            a.append(temp.val)
            temp = temp.next
        i = 0
        j = len(a) - 1
        while i < j:
            Sum = a[i] + a[j]
            Max = max(Sum, Max)
            i += 1
            j -= 1
        return Max
