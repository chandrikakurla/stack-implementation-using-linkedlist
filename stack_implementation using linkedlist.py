class StackNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack_LinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if(self.head==None):
            return True
        else:
            return False
    def push(self,newdata):
        newnode=StackNode(newdata)
        if self.head is None:
            self.head=newnode
            return print("%d is pushed into stack"%(newnode.data))
        newnode.next=self.head
        self.head=newnode
        return print("%d is pushed into stack"%(newnode.data))
    def pop(self):
        if(self.isEmpty()):
            return print("stack is empty")
        popped=self.head.data
        self.head=self.head.next
        return print("%d is popped from stack"%popped)
    def peek(self):
        if(self.isEmpty()):
            return print("stack is empty")
        return print("top element is %d"%self.head.data)
stack=Stack_LinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.peek()



