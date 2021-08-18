class Stack:

    def __init__(self):
        self.elements = []

    def push(self, element):
        return self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return None

    def peek(self):
        if not self.is_empty():
            last_element = len(self.elements) - 1
            return self.elements[last_element]
        return None

    def is_empty(self):
        return len(self.elements) == 0
