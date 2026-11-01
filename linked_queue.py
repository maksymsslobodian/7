class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Помилка: черга порожня")
            return None
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return value

    def display(self):
        if self.is_empty():
            print("Черга порожня")
            return
        items = []
        current = self.head
        while current is not None:
            items.append(str(current.data))
            current = current.next
        print("Черга:", " -> ".join(items) + " -> None")


if __name__ == "__main__":
    print("\n=== Черга на вузлах ===")
    q = LinkedQueue()
    for x in [12, 25, 8]:
        q.enqueue(x)
    q.display()
    print("Кількість елементів:", q.size())

    print("Видалено:", q.dequeue())
    q.display()
    print("Кількість елементів:", q.size())

    q.enqueue(40)
    q.display()
