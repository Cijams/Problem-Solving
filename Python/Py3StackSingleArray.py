# Simulate a C style array of 0's.
class Array(list):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def append(self, element):
        if len(self) < self.size:
            list.append(self, element)
        else:
            return False


class TripleStack:
    def __init__(self):
        self.size_of_each_array = [0, 34, 67]
        self.my_array = Array(99)
        self.number_of_stacks = 3
        for i in range(100):
            self.my_array.append(0)

    def __str__(self):
        string = ""
        for i in self.my_array:
            string += str(i) + ", "
        return string[:-2]

    def push(self, stack_num, data):
        if not 1 <= stack_num <= 3:
            raise IndexError
        stack_num -= 1
        if self.size_of_each_array[0] >= 34 or self.size_of_each_array[1] >= 67 \
                or self.size_of_each_array[2] >= 99:
            raise IndexError
        else:
            self.my_array[int(self.size_of_each_array[stack_num])] = data
            self.size_of_each_array[stack_num] += 1

    def pop(self, stack_num):
        if not 1 <= stack_num <= 3:
            raise IndexError
        try:
            pos = self.my_array.index(self.my_array[self.size_of_each_array[0]-1])
            del self.my_array[pos]
            self.my_array.insert(pos, 0)
        except IndexError as e:
            return e

    def peek(self, stack_num):
        if not 1 <= stack_num <= 3:
            raise IndexError
        stack_num -= 1
        return self.my_array[self.size_of_each_array[stack_num]-1]

    @staticmethod
    def is_empty(stack_num):
        if stack_num == 0:
            return stack_num == 0
        if stack_num == 1:
            return stack_num == 34
        if stack_num == 0:
            return stack_num == 67
        raise IndexError

    @staticmethod
    def is_full(stack_num):
        if stack_num == 0:
            return not stack_num <= 34
        if stack_num == 1:
            return not stack_num <= 67
        if stack_num == 0:
            return not stack_num <= 99
        raise IndexError


# Testing
ts = TripleStack()
ts.push(2, 15)
ts.push(2, 16)
ts.push(1, 3)
ts.push(1, 3)
ts.push(3, 99)
print(ts)
for i in range(3):
    ts.push(1, i)
print(ts)

print(ts.peek(2))
print(ts.peek(1))
print(ts.peek(3))
print(ts.is_full(1))

print(ts)
ts.pop(1)
print(ts)
