from typing import List


class SortStrategy:
    def sort(self, dataset: List[int]) -> List[int]:
        raise NotImplementedError


class BubbleSort(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        n = len(dataset)
        for i in range(n):
            for j in range(0, n-i-1):
                if dataset[j] > dataset[j + 1]:
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
        return dataset


class QuickSort(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        if len(dataset) <= 1:
            return dataset
        else:
            pivot = dataset.pop()
            greater = [element for element in dataset if element > pivot]
            lesser = [element for element in dataset if element <= pivot]
            return self.sort(lesser) + [pivot] + self.sort(greater)


class SortedData:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
        self._data = []

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def add_data(self, data: List[int]):
        self._data.extend(data)

    def sort_data(self) -> List[int]:
        return self._strategy.sort(self._data)


if __name__ == "__main__":
    data = SortedData(BubbleSort())
    data.add_data([23, 12, 5, 29, 7, 9])
    print("Sorted using BubbleSort:", data.sort_data())

    data.set_strategy(QuickSort())
    print("Sorted using QuickSort:", data.sort_data())
