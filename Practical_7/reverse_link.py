class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current is not None:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev one step
        current = next_temp       # Move current one step
    
    return prev  # prev is the new head of the reversed list

# Helper functions
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

# Predefined list
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original List:")
print_linked_list(head)

reversed_head = reverseList(head)

print("\nReversed List:")
print_linked_list(reversed_head)