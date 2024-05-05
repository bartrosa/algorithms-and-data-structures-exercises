class NumberCollection:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return NumberIterator(self._data)


class NumberIterator:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __next__(self):
        try:
            value = self._data[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()


if __name__ == "__main__":
    collection = NumberCollection([1, 2, 3, 4, 5])
    for number in collection:
        print(number)
