class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast pointer n nodes ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the nth node
    slow.next = slow.next.next

    return dummy.next

# Helper functions for testing
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Predefined test
values = [1, 2, 3, 4, 5]
n = 2
print("Original List:")
print_linked_list(create_linked_list(values))

head = create_linked_list(values)
new_head = removeNthFromEnd(head, n)

print(f"\nAfter removing {n}th node from end:")
print_linked_list(new_head)