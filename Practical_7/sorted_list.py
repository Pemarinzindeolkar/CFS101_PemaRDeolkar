class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return dummy.next

# Helper functions
def create_linked_list(values):
    if not values:
        return None
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
list1_values = [1, 2, 4]
list2_values = [1, 3, 4]

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

print("List 1:")
print_linked_list(list1)
print("\nList 2:")
print_linked_list(list2)

merged_head = mergeTwoLists(list1, list2)
print("\nMerged List:")
print_linked_list(merged_head)