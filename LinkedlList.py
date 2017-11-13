
class Node:

    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, node):
        self.length += 1
        if not self.head:
            self.head = self.tail = Node(node, None, None)
        else:
            self.tail.next = self.tail = Node(node, None, self.tail)

    def push(self, node):
        self.length += 1
        if not self.head:
            self.tail = self.head = Node(node, None, None)
        else:
            self.head = Node(node, self.head, None)
            self.head.next.prev = self.head

    def insert(self, position, node):
        if not self.head:
            self.length += 1
            self.head = self.tail = Node(node, None, None)
            return
        if position == 0:
            self.length += 1
            self.head = Node(node, self.head, None)
            self.head.next.prev = self.head
            return
        if position == self.length:
            self.length += 1
            self.tail.next = self.tail = Node(node, None, self.tail)
            return
        if position > self.length:
            raise IndexError
        current = self.head
        current_position = 0
        while current.next != None:
            current_position += 1
            if current_position == position:
                self.length += 1
                current.next = Node(node, current.next, current)
                current.next.next.prev = current.next
                break
            current = current.next

    def pop(self):
        if not self.head:
            raise IndexError
        if self.length == 1:
            result = self.head.data
            self.tail = self.head = None
            self.length = 0
            return result
        result = self.tail.data
        self.tail = self.tail.prev
        self.tail.next.prev = None
        self.tail.next = None
        self.length -= 1
        return result

    def remove(self, item):
        if not self.head:
            return
        if self.length < item or item < 0:
            raise IndexError
        if self.length == 1:
            self.length = 0
            self.head = self.tail = None
            return
        if item == self.length:
            pass

        current = self.head
        current_position = 0
        while current.next != None:
            current_position += 1
            if current_position == item:
                self.length -= 1
                tmp = current.next
                current.next = current.next.next
                current.next.prev = current
                tmp.next = tmp.prev = None
                break
            current = current.next

    def clear(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        if self.head:
            current = self.head
            arr = []
            arr.append(current.data)
            while current.next != None:
                current = current.next
                arr.append(current.data)
            return 'LinkedList = [' + arr.__str__() + ']'
        else:
            return 'LinkedList = [ ]'


if __name__ == "__main__":
    ll = LinkedList()
    ll.add('One')
    ll.add('Two')
    ll.add('Three')
    ll.push('Four')
    ll.insert(3, 'Five')
    ll.remove(2)
    print(ll)
    print(len(ll))
    for iterator in range(len(ll)-1):
        print(ll.pop())
    ll.remove(0)
    print(ll)
    print(len(ll))

