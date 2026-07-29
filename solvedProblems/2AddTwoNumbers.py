# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1str = []
        num2str = []
        tempNode = l1
        while tempNode:
            num1str.insert(0, tempNode.val)
            tempNode = tempNode.next
        print(num1str)
        tempNode = l2
        while tempNode:
            num2str.insert(0, tempNode.val)
            tempNode = tempNode.next
        print(num2str)
        num1 = int("".join(map(str, num1str)))
        num2 = int("".join(map(str, num2str)))
        sum = num1+num2
        sumStr = str(sum)
        numDigits = len(sumStr)
        if numDigits == 1:
            newNode = ListNode(int(sumStr[0]), None)
        else:
            for i in range(0,numDigits):
                if i == 0:  #first digit
                    newNode = ListNode(int(sumStr[i]), None)
                    tempNode = newNode
                elif i == numDigits - 1:    #last digit
                    newNode = ListNode(int(sumStr[i]), tempNode)
                else:   #other digits
                    newNode = ListNode(int(sumStr[i]), tempNode)
                    tempNode = newNode
        return newNode



l1_3 = ListNode(3,None)
l1_2 = ListNode(4,l1_3)
l1_1 = ListNode(2,l1_2)

l2_3 = ListNode(4,None)
l2_2 = ListNode(6,l2_3)
l2_1 = ListNode(5,l2_2)

solution = Solution
solution.addTwoNumbers(solution, l1_1, l2_1)

        