from common import Node


class StackAsList:
    def __init__(self):
        self._top = None
        self._min = None

    def push(self, item):
        if self._min is None:
            self._min = item
        elif item < self._min:
            self._min = item
        node = Node(item)
        node.next = self._top
        self._top = node

    def pop(self):
        if self._top is None:
            return ValueError('Empty Stack')
        result = self._top
        self._top = self._top.next
        return result.data

    def min(self):
        return self._min

    def is_empty(self):
        return self._top is None

    def size(self):
        count = 0
        current = self._top
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        current = self._top
        result = ''
        while current is not None:
            result += f'[{current.data}]'
            if current.next is not None:
                result += '->'
            current = current.next
        return result


if __name__ == '__main__':
    sl = StackAsList()
    print(f'Initially stack is empty ? {sl.is_empty()}')
    sl.push(20)
    sl.push(11)
    sl.push(9)
    print(f'Size of the stack: {sl.size()}')
    sl.pop()
    print(f'Stack: {sl}')
    print(f'Is stack empty: {sl.is_empty()}')
