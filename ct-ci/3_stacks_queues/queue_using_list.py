"""
FIFO Queue as list. The implementation is similar to Linked list.
Note that we need make sure that first and last nodes are always updated to avoid bugs.
"""

from common import Node


class QueueAsList:
    def __init__(self):
        self._first = None
        self._last = None

    def add(self, item):
        node = Node(item)
        node.next = self._first
        self._first = node
        # Single item in the Q
        if self._first.next is None:
            self._last = node

    def remove(self):
        if self._first is None:
            return ValueError('Empty Queue')
        result = self._last
        current = self._first
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        self._last = previous
        previous.next = None
        return result.data

    def is_empty(self):
        return self._first is None

    def size(self):
        current = self._first
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self._first
        res = ''
        while current is not None:
            res += f'[{current.data}]'
            if current.next is not None:
                res += '->'
            current = current.next
        return res


if __name__ == '__main__':
    ql = QueueAsList()
    ql.add(10)
    ql.add(11)
    ql.add(20)
    ql.add(33)
    print(f'Queue: {ql}')
    print(f'After remove: {ql.remove()}')
    print(f'After remove: {ql.remove()}')
    print(f'Q empty: {ql.is_empty()}')
    print(f'Q size: {ql.size()}')
