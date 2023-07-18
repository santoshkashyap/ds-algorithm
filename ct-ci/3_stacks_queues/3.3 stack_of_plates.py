from common import Node
from stack_using_list import StackAsList


class SetOfStacks:
    def __init__(self, capacity):
        self._capacity = capacity
        self._stacks = []

    def push(self, item):
        index = self.size() // self._capacity
        if self.size() == 0 or (len(self._stacks) - 1) < index:
            self._stacks.append(StackAsList())
        self._stacks[index].push(item)

    def pop(self):
        index = self.size() // self._capacity
        self._stacks[index].pop()

    def size(self):
        count = 0
        for stack in self._stacks:
            count += stack.size()
        return count

    def capacity(self):
        return self._capacity

    def __str__(self):
        result = ''
        for stack in self._stacks:
            result += str(stack)
            result += '\n'
        return result


if __name__ == '__main__':
    ss = SetOfStacks(3)
    ss.push(10)
    ss.push(101)
    ss.push(22)
    ss.push(33)
    ss.push(144)

    print(f'Set of stacks: {ss}')
    ss.pop()
    print(f'Set of stacks after removal: {ss}')
