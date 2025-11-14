Practical 4
singly_linked_list.py<br>
Define a Node class with data and a pointer to the next node.<br>
Define a LinkedList class with methods to check if empty, insert nodes at the front or end, delete the front node, search for a value, and display all elements.<br>
Create a linked list instance, add nodes at the end and front.<br>
Display the list elements as a chain.<br>
Search for a value in the list, returning True or False.<br>
Delete the front node and display the updated list.<br>
Output<br>
1

-1

3 -> 4 -> 1

<img src="singly.png" alt="Output Screenshot" width="300"> <br>

reverse_linked_linked.py<br>
First, use the ListNode class to make nodes for your singly linked list, giving each node a value and a link to the next node.<br>
To reverse a list, create some nodes, join them together. <br>
For merging, create two sorted lists using ListNode objects, link each list.<br>
To remove the nth node from the end, build a list with ListNode.<br>
You can also use the Solution class method in exactly the same way to reverse a list. <br>
Always create your test linked lists first, run the function, and print each value to see that your code works right.<br>

Binary_search_function.py<br>
Array must be sorted.<br>
Set left and right pointers (start and end of array).<br>
Keep repeating these steps:<br>
Find the middle index of the current search area.<br>
If the middle value equals your target, you're done—return its index.<br>
If the middle value is less than your target, focus only on the right half for the next round.<br>
If the middle value is greater than your target, focus only on the left half for the next round.<br>
Do this until you find the target or there’s nothing left to search.<br>
If target is not found, return -1.<br>
Output<br>
Step 1: left=0, right=8, mid=4

Current subarray: [1, 3, 5, 7, 9, 11, 13, 15, 17]

9 < 13, searching right half.

Step 2: left=5, right=8, mid=6

Current subarray: [11, 13, 15, 17]

Found 13 at index 6 after 2 steps.

<img src="binary.png" alt="Output Screenshot" width="300"> <br>

further_exercises.py<br>
Create a linked list and add values to it.<br>
Use a function to find the middle element.<br>
Set up a linked list and check if it has a cycle. <br>
Build a linked list with some repeated values and remove all duplicates. <br>
Make two sorted linked lists and merge them into one sorted list. <br>
After each operation, print the linked list to see the result.<br>
Output<br>
Middle Element: 6

Has Cycle: True

Before Removing Duplicates:

1 -> 3 -> 2 -> 3 -> 4 -> 2 -> 5 -> 3 -> 1 -> 7 -> None

After Removing :

1 -> 3 -> 2 -> 4 -> 5 -> 7 -> None

Merged Sorted List:

1 -> 2 -> 3 -> 4 -> 7 -> 8 -> None

<img src="further.png" alt="Output Screenshot" width="300"> <br>


