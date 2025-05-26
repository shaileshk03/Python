from contextlib import nullcontext

from Data_Structures_Algorithms.Array.Find_Smallest_Largest import find_smallest_num


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add first
    def add_first(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # Add Last
    def add_last(self, data):
        new_node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Print LinkedList
    def print_list(self):
        if self.head is None:
            print("LL is empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print()

    # Add LinkedList
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

    # Remove first
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

    # Remove last
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

    # Iterative search
    def iter_search(self, key):
        temp = self.head
        i = 0
        while temp is not None:
            if temp.data == key:
                return i
            temp = temp.next
            i += 1
        return -1

    # Recursive search helper function
    def helper_fun(self, head, key):
        if head is None:
            return -1
        if head.data == key:
            return 0
        idx = self.helper_fun(head.next, key)
        if idx == -1:
            return -1
        return idx + 1

    # Recursive Search function
    def rec_search(self, key):
        return self.helper_fun(self.head, key)

    # Reverse Linked List
    def reverse_linked_list(self):
        prev = None
        current = self.tail = self.head
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            # update head
        self.head = prev

    # Delete nth linkedList from end
    def delete_nth_from_end(self, n):
        # calculate size
        size = 0
        # temp pointing to head
        temp = self.head

        while temp is not None:
            temp = temp.next
            size += 1

        if n == size:
            self.head = self.head.next  # Remove first
            return

        # size-n
        i = 1
        i_to_find = size - n
        prev = self.head

        while i < i_to_find:
            prev = prev.next
            i += 1

        prev.next = prev.next.next
        return

    # Find the middle of the LinkedList (slow fast approach
    def find_mid(head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # 1
            fast = fast.next.next  # 2
        return slow  # slow is midNode

    # Check palindrome
    def check_palindrome(head):
        if head is None or head.next is None:
            return True

        # step1 - Find middle
        mid_node = head.find_mid(head)

        # step2 - reverse 2nd half
        prev = None
        current = mid_node
        next_node = None

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        right = prev
        left = head

        # step3 - check left half and right half
        while right is not None:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next

        return True

if __name__ == "__main__":
    ls = LinkedList()
    ls.add_first(2)
    ls.add_first(1)
    ls.add_last(3)
    ls.add_last(4)
    ls.add_last(5)
    ls.add(2, 3)

    ls.print_list()
    print("Size of LinkedList is : " + str(ls.size))

    # ls.remove_last()
    # ls.print_list()
    # ls.reverse_linked_list()
    ls.delete_nth_from_end(3)
    ls.print_list()