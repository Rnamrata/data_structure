class LinkedList:
    def __init__(self, data=None):
        self.node = data
        self.next = None
        self.head = None

    def append_to_list(self, data):
        if self.head is None:
            self.head = LinkedList(data)
        else:
            search_value = self.head

            while search_value.next is not None:
                search_value = search_value.next

            search_value.next = LinkedList(data)
            # print(search_value.next)

    def print_list(self):
        list_value = self.head
        print("Printing data:")

        while list_value.next is not None:
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
        linked_list.append_to_list(value)
        condition = check_confirmation()

    linked_list.print_list()

