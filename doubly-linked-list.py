class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_from_beginning(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_from_beginning(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
            count += 1
            itr = itr.next

        # this is an alternative way of doing it but I like the way I did it above better.
        # itr = self.head
        # while itr.next:
        #     if itr.next.data == data:
        #         itr.next = itr.next.next
        #         break
        #     itr = itr.next

    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        return itr

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.next
        print(llstr)

    def print_forward(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.next
        print(llstr)

    def print_backwards(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.get_last_node()
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.prev
        print('Linked list in reverse: ', llstr)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backwards()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    # ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
