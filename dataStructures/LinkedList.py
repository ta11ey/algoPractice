from . ListNode import ListNode

def build(arr):
    current = ListNode()
    head = ListNode(arr[0], current)

    for i in arr[1:-1] :
        current.val = i
        current.next = ListNode()
        current = current.next

    current.val = arr[-1]
    current.next = None

    return head
