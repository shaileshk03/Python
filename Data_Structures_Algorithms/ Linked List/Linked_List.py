class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        if self.head is None:
            print("LL is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print()

    def add(self, idx, data):
        if idx == 0:
            self.add_first(data)
            return
        new_node = Node(data)
        self.size += 1
        temp = self.head
        for i in range(idx - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def remove_first(self):
        if self.size == 0:
            print("LL is empty")
            return float('-inf')
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            return val
        val = self.head.data
        self.head = self.head.next
        return val

    def remove_last(self):
        if self.size == 0:
            print("LL is empty")
            return float('-inf')
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            self.size = 0
            return val
        prev = self.head
        for i in range(self.size - 2):
            prev = prev.next
        val = prev.next.data
        prev.next = None
        self.tail = prev
        self.size -= 1
        return val

    def iter_search(self, key):
        temp = self.head
        i = 0
        while temp is not None:
            if temp.data == key:
                return i
            temp = temp.next
            i += 1
        return -1

    def helper_fun(self, head, key):
        if head is None:
            return -1
        if head.data == key:
            return 0
        idx = self.helper_fun(head.next, key)
        if idx == -1:
            return -1
        return idx + 1

    def rec_search(self, key):
        return self.helper_fun(self.head, key)

if __name__ == "__main__":
    ls = LinkedList()
    ls.add_first(2)
    ls.add_first(1)
    ls.add_last(3)
    ls.add_last(4)
    ls.add(2, 3)

    ls.print_list()
    print("Size of LinkedList is : " + str(ls.size))

    ls.remove_last()
    ls.print_list()