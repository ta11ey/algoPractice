# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

from algoPractice.dataStructures.ListNode import ListNode

def dummyInsert(head: ListNode, item: ListNode):
    dummy = ListNode()
    current = dummy
    current.next = head

    while current.next and current.next.val < item.val:
        current = current.next

    item = ListNode(item.val, current.next)
    current.next = item

    return dummy.next


def exec(head):
#   sorted part
    sortedHead = ListNode(head.val, None)
#   Current
    current = head
#   Unsorted
    while current.next is not None:
        sortedHead = dummyInsert(sortedHead, current.next)
        current = current.next

    return sortedHead

