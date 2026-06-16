from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# Helper function to create linked list from list
def createLinkedList(arr):
    dummy = ListNode()
    curr = dummy

    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next

    return dummy.next


# Helper function to convert linked list back to list
def linkedListToArray(head):
    result = []

    while head:
        result.append(head.value)
        head = head.next

    return result


# Test
head = createLinkedList([0,1,2,3])

solution = Solution()

reversed_head = solution.reverseList(head)

assert linkedListToArray(reversed_head) == [3,2,1,0]

print("Test passed")
        