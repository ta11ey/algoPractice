from . algorithms import linkedList_insertionSort
from . dataStructures import LinkedList
from . utilities import linkedLists
from . datasets.lists import list1

def insertionSort():
    original = LinkedList.build(list1)
    answer = linkedList_insertionSort.exec(original)
    return f'Original: {linkedLists.visualize(original)} \n Answer: {linkedLists.visualize(answer)}'

