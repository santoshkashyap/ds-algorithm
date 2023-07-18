from stack_using_list import StackAsList

if __name__ == '__main__':
    sl = StackAsList()
    sl.push(12)
    sl.push(19)
    sl.push(111)
    sl.push(32)
    sl.push(55)

    print(f'Stack : {sl} and min element: {sl.min()}')
    sl.pop()
    print(f'Stack after removal: {sl}')
