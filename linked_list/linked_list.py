class Node:
    def __int__(self, data):
        self.node = data
        self.next = None

        return self

    def return_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        listValue = self.head
        print("Printing data:")

        while (listValue):
            print(listValue.nodeValue)
            listValue = listValue.next


def check_confirmation(confirmation):
    confirmation == input("do you want to continue? (y/n): ")

    if confirmation == 'y' or confirmation == 'Y':
        return True
    else:
        return False


if __name__ == "__main__":
    list = LinkedList()
    i = 0
    confirmation = ''
    condition = True

    while condition:
        value = input('Input the value: ')
        list.head = Node.__int__(list.head, value)

        if i == 0:
            list.head.next = list.head
        else:
            list.head.next = Node.return_next()

        i += 1
        condition = check_confirmation(confirmation)

