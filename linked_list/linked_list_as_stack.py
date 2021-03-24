class Node:
    def __init__(self, data=None):
        self.node = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_first_list(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            search_value = self.head
            self.head = Node(data)
            self.head.next = search_value

    def print_list(self):
        list_value = self.head
        print("Printing data:")

        while list_value is not None:
            print(list_value.node)
            # print(list_value.next)
            list_value = list_value.next


def check_confirmation():
    confirmation = input("do you want to continue? (y/n): ")

    if confirmation == 'y' or confirmation == 'Y':
        return True
    else:
        return False


if __name__ == "__main__":
    linked_list = LinkedList()
    condition = True

    while condition:
        value = input('Input the value: ')
        linked_list.add_to_first_list(value)
        condition = check_confirmation()

    linked_list.print_list()

