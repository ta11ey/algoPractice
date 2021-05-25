from typing import List
from dataset import dataset1, dataset2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeLinkedList(arr):
    current = ListNode()
    head = ListNode(dataset1[0], current)

    for i in dataset1[1:-1] :
        current.val = i
        current.next = ListNode()
        current = current.next

    current.val = dataset1[-1]
    current.next = None

    return head

linkedList1 = makeLinkedList(dataset1)
linkedList2 = makeLinkedList(dataset2)

def dummyInsert(head: ListNode, item: ListNode):
    dummy = ListNode(0, head)
    newInsert = ListNode(item.val)
    current = dummy

    while current.next and current.next.val < item.val:
        current = current.next

    newInsert.next = current.next
    current.next = item

    return dummy.next


def insertionSort(head):
    sortedHead = ListNode(head.val, None)
    current = head

    while current.next is not None:
        sortedHead = dummyInsert(sortedHead, current)
        current = current.next

    return sortedHead

insertionSort(linkedList1)
