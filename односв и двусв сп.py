class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next

    def insert_after(self, node_data, new_data):
        current = self.head
        while current:
            if current.data == node_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if not self.head or not self.head.next:
            return

        def merge_sort(head_ref):
            if not head_ref or not head_ref.next:
                return head_ref

            middle = get_middle(head_ref)
            next_to_middle = middle.next
            middle.next = None

            left = merge_sort(head_ref)
            right = merge_sort(next_to_middle)

            sorted_list = merge(left, right)
            return sorted_list

        def get_middle(head):
            if not head:
                return head

            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left

            if left.data <= right.data:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)

            return result

        self.head = merge_sort(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Пример использования
linked_list = LinkedList()
linked_list.append(4)
linked_list.append(2)
linked_list.append(1)
linked_list.append(3)

print("Список до удаления:")
linked_list.print_list()
linked_list.delete(2)
print("Список после удаления:")
linked_list.print_list()

print("Список до вставки:")
linked_list.print_list()
linked_list.insert_after(1, 5)
print("Список после вставки:")
linked_list.print_list()

print("Список до переворота:")
linked_list.print_list()
linked_list.reverse()
print("Список после переворота:")
linked_list.print_list()

print("Список до сортировки:")
linked_list.print_list()
linked_list.sort()
print("Список после сортировки:")
linked_list.print_list()