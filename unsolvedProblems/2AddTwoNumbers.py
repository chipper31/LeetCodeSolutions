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
        #print(num1str)
        tempNode = l2
        while tempNode:
            num2str.insert(0, tempNode.val)
            tempNode = tempNode.next
        #print(num2str)
        num1 = int("".join(map(str, num1str)))
        num2 = int("".join(map(str, num2str)))
        sum = num1+num2
        sumStr = str(sum)
        sumList = []
        numDigits = len(sumStr)
        for i in range(0,numDigits):
            #sumList.append(sumStr[numDigits-1-i])
            if i == 0:
                currentNode:ListNode = ListNode(sumStr[i], None)
            elif i == numDigits - 1:
                newNode:ListNode = ListNode(sumStr[i], currentNode)
                currentNode = None
            else:
                newNode:ListNode = ListNode(sumStr[i], currentNode)
                currentNode:ListNode = ListNode(sumStr[i+1], None)
        #print(sumList)
        return newNode



l1_3 = ListNode(3,None)
l1_2 = ListNode(4,l1_3)
l1_1 = ListNode(2,l1_2)

l2_3 = ListNode(4,None)
l2_2 = ListNode(6,l2_3)
l2_1 = ListNode(5,l2_2)

solution = Solution
solution.addTwoNumbers(solution, l1_1, l2_1)

        