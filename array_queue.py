class ArrayQueue:
    def __init__(self, capacity=13):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("Помилка: черга переповнена")
            return
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Помилка: черга порожня")
            return None
        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return value

    def display(self):
        if self.is_empty():
            print("Черга порожня")
            return
        items = []
        index = self.head
        for _ in range(self.count):
            items.append(str(self.data[index]))
            index = (index + 1) % self.capacity
        print("Черга:", " <- ".join(items))
        print(f"Head = {self.head}, Tail = {self.tail}")


if __name__ == "__main__":
    print("=== Черга на масиві ===")
    q = ArrayQueue(13)
    for x in [6, 4, 6, 2, 7]:
        q.enqueue(x)
    q.display()
    print("Кількість елементів:", q.size())

    print("Видалено:", q.dequeue())
    print("Видалено:", q.dequeue())
    q.display()
    print("Кількість елементів:", q.size())
