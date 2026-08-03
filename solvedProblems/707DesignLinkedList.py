class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        if index == 0:
            return self.head.val
        
        currNode = self.head.next
        for i in range(1,index):
            if currNode:
                currNode = currNode.next
            else:
                return -1

        if currNode:
            return currNode.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head:
            newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
            return
        
        currNode = self.head
        while currNode.next:
            currNode = currNode.next
        currNode.next = newNode
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        newNode = ListNode(val)
        currNode = self.head

        for i in range(0,index-1):
            currNode = currNode.next
        newNode.next = currNode.next
        currNode.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        
        if index == 0:
            self.head = self.head.next
            return
        
        currNode = self.head
        for i in range(0,index-1):
            currNode = currNode.next
        if currNode.next:
            currNode.next = currNode.next.next
        else:
            currNode.next = None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)