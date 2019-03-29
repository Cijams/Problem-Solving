class StackOfStacks:
    def __init__(self):
        self.king_stack = [[]]
        self.max_size = 4
        self.current_size = 0
        self.current_stack = 0

    def __str__(self):
        string = ""
        for i in self.king_stack:
            string += str(i) + ", "
        return string[:-2]

    def push(self, data):
        if self.current_size < self.max_size:
            self.king_stack[self.current_stack].append(data)
            self.current_size += 1
        else:
            self.current_stack += 1
            self.current_size = 0
            self.king_stack.append([])
            self.push(data)

    def pop(self):
        if not self.is_empty():
            self.king_stack[self.current_stack].pop()
            if len(self.king_stack[self.current_stack]) == 0:
                del self.king_stack[self.current_stack]
                self.current_stack -= 1
                self.current_size = self.max_size

    def peek(self):
        print(self.king_stack[self.current_size])

    def is_empty(self):
        return False if self.king_stack else True


ks = StackOfStacks()
print(ks.is_empty())
ks.push(3)
ks.push(3)
ks.push(3)
ks.push(3)
ks.push(4)
print(ks)
ks.peek()
print(ks.is_empty())
print()
print(ks)

print("_________")
print("KS BEFORE POP:")
print(ks)
print("_________")
print("KS AFTER POP:")
ks.pop()
print(ks)

print("")
print("_________")
print("KS BEFORE POP:")
print(ks)
print("_________")
print("KS AFTER POP:")
ks.pop()
print(ks)
ks.pop()
ks.pop()
ks.pop()
print(ks)
ks.pop()
print()
for i in range(0, 7):
    ks.push(i)
print(ks)
ks.pop_at(1)
print(ks)