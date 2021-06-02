from algoPractice.dataStructures.ListNode import ListNode

def visualize(linkedList: ListNode):
    output = linkedList.val
    head = linkedList.next
    while (head.val):
        output = f'{output}  ->  {head.val}'
        if (head.next):
            head = head.next
        else:
            break

    return output
