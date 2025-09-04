class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None


ll = LinkedList()
for i in [2, 4, 6, 8, 10]:
    ll.append(i)
print("Middle Element:", ll.find_middle())  

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                return True
        return False

ll = LinkedList()
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)

ll.head.next.next.next = ll.head

print("Has Cycle:", ll.has_cycle())  

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



ll = LinkedList()
for i in [1, 3, 2, 3, 4, 2, 5, 3, 1, 7]:
    ll.append(i)

print("Before Removing Duplicates:")
ll.print_list()

ll.remove_duplicates()

print("After Removing :")
ll.print_list()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


a = Node(1)
a.next = Node(3)
a.next.next = Node(7)

b = Node(2)
b.next = Node(4)
b.next.next = Node(8)

merged = merge_sorted_lists(a, b)
print("Merged Sorted List:")
print_list(merged)