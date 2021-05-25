from typing import List
from dataset import dataset1, dataset2

class ListNode:
    def __init__(self, val=None, next=None):
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
    dummy = ListNode()
    current = dummy
    current.next = head

    while current.next and current.next.val < item.val:
        current = current.next

    item = ListNode(item.val, current.next)
    current.next = item

    return dummy.next


def insertionSort(head):
#   sorted part
    sortedHead = ListNode(head.val, None)
#   Current
    current = head
#   Unsorted
    while current.next is not None:
        sortedHead = dummyInsert(sortedHead, current.next)
        current = current.next

    return sortedHead

insertionSort(linkedList1)
