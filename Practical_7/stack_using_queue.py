from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.put(x)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if self.q1.empty():
            print("Stack is empty! Cannot pop.")
            return None
        return self.q1.get()

    def top(self) -> int:
        if self.q1.empty():
            print("Stack is empty! No top element.")
            return None
        return self.q1.queue[0]

    def empty(self) -> bool:
        return self.q1.empty()


stack = MyStack()

print("Pushing elements: 1, 2, 3")
stack.push(1)
stack.push(2)
stack.push(3)

print("Current Top Element:", stack.top())  
print("Popping element:", stack.pop())      
print("New Top Element:", stack.top())      
print("Is stack empty?", stack.empty())     

print("Popping all elements...")
stack.pop()
stack.pop()

print("Is stack empty now?", stack.empty())  
print("Trying to pop from empty stack:")
stack.pop()  