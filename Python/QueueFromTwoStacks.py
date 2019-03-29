class Stack():
    def __init__(self):
        self.stack = []

    def __str__(self):
        string = ""
        for i in self.stack:
            string += str(i) + ", "
        return string[:-2]

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()


class QueueStacks:
    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()
        self.left = True

    def push(self, data):
        if self.left:
            self.stack_one.push(data)
        else:
            self.stack_two.push(data)

    def pop(self):
        if self.left:
            self.swap(self.stack_one, self.stack_two)
            self.left = False
            return self.stack_two.pop()
        else:
            self.swap(self.stack_two, self.stack_one)
            self.left = True
            self.stack_two.pop()
            return self.stack_one.pop()

    @staticmethod
    def swap(s1, s2):
        while s1:
            temp = s1.pop()
            if temp is None:
                break
            s2.push(temp)


qs = QueueStacks()
qs.push(3)
qs.push(1)
qs.push(2)
print(qs.pop())
print(qs.pop())
print(qs.pop())

# just like a queue