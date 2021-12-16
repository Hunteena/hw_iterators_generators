class FlatIterator:
    def __init__(self, nested_list):
        self.stack = [nested_list]

    def __iter__(self):
        self.cursor = self.stack[0]
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        while isinstance(self.cursor, list):
            if len(self.cursor) > 1:
                self.stack.append(self.cursor[1:])
            self.cursor = self.cursor[0]
        next_item = self.cursor
        self.cursor = self.stack.pop()
        return next_item


def flat_generator(nested_list):
    if isinstance(nested_list, list):
        for nested in nested_list:
            for item in flat_generator(nested):
                yield item
    else:
        yield nested_list
