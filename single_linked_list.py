class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Adds an element at the beggining of the list
        :param data:
        :return:
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def get_len(self):
        """
        Returns the length of Linked List
        :return:
        """
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr:
                count += 1
                itr = itr.next
            return count

    def insert_at_end(self, data):
        """
        Adds an element at the end of the list
        :param data:
        :return:
        """
        if self.head is None:
            return
        else:
            itr = self.head
            count = 0
            while itr:
                if count == self.get_len() - 1:
                    node = Node(data)
                    itr.next = node
                    break
                count += 1
                itr = itr.next

    def print(self):
        """
        Prints every object in Linked List.
        :return: 
        """
        if self.head is None:
            print("[]")
            return
        itr = self.head
        iter_str = ""
        while itr:
            iter_str += f"{itr.data}-->"
            itr = itr.next
        print(iter_str)

    def clear(self):
        """
        Removes all the elements from the list
        :return:
        """
        self.head = None

    def count(self, data):
        """
        Returns the number of elements with the specified value
        :return:
        """
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr:
                if itr.data == data:
                    count += 1
                itr = itr.next
            return count

    def extent(self, data):
        """
        Add the elements of a list (or any iterable), to the end of the current list
        :return:
        """
        count = 0
        if self.head is None:
            return count
        else:
            itr = self.head
            while itr:
                if count == self.get_len() - 1:
                    for item in data:
                        self.insert_at_beginning(item)
                    break
                count += 1
                itr = itr.next

    def index(self, data):
        """
        Returns the index of the first element with the specified value
        :return:
        """
        count = 0
        if self.head is None:
            return
        else:
            itr = self.head
            while itr:
                if itr.data == data:
                    return count
                count += 1
                itr = itr.next

    def insert_at_index(self, index, data):
        """
        Adds an element at the specified position
        :return:
        """
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def pop(self, index):
        """
        Removes the element at the specified position
        :return:
        """
        if index < 0 or index > self.get_len():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 2:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def remove(self, data):
        """
        Removes the first item with the specified value
        :return:
        """
        if self.head is None:
            return
        if self.head == data:
            self.head = self.head.next
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning("test")
    ll.insert_at_beginning("test1")
    ll.insert_at_beginning("test2")
    ll.insert_at_beginning("test4")
    ll.insert_at_beginning("test")
    ll.insert_at_beginning("test")
    ll.insert_at_end("ttes222")
    ll.insert_at_end("test2222")
    print("count " + str(ll.count("test4")))
    print(ll.get_len())
    ll.print()
    ll.clear()
    print(ll.get_len())
    ll.print()
    ll.insert_at_beginning("test")
    ll.insert_at_beginning("test")
    ll.insert_at_beginning("test1")
    ll.insert_at_end("test2222")
    ll.extent([1,2,3,4,5])
    ll.print()
    print(ll.index("test"))
    ll.insert_at_index(5, 5)
    ll.print()
    ll.pop(0)
    ll.print()
    ll.pop(5)
    ll.print()
    ll.remove("test")
    ll.print()
