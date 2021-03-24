class Node:
    def __init__(self, data=None):
        self.node = data
        self.next = None


class LinkedList:
    iteration = 0

    def __init__(self):
        self.head = None

    def add_to_list(self, data, position):
        if position > (LinkedList.iteration+1):
            print('Invalid input. Please try again!')

        else:
            if self.head is None:
                self.head = Node(data)
            else:
                search_value = self.head

                if search_value.next is None:
                    if position is 1:
                        self.head = Node(data)
                        self.head.next = search_value
                    else:
                        search_value.next = Node(data)
                else:
                    j = 1
                    while search_value.next is not None:
                        if position is j:
                            temporary_node = search_value
                            search_value = Node(data)
                            search_value.next = temporary_node
                            break
                        else:
                            search_value = search_value.next
                            j += 1
            LinkedList.iteration += 1

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
    i = 0
    while condition:
        value = input('Input the value: ')
        position = int(input('Input the position: '))

        linked_list.add_to_list(value, position)
        condition = check_confirmation()

    linked_list.print_list()

