#!/usr/bin/python3

from dataclasses import dataclass

import matplotlib.pyplot as plt


@dataclass()
class BarGraph:
    _data: list
    _keys: list
    _type_of_sequence: str

    def display(self):
        print(self._keys, self._data)
        plt.bar(self._keys, self._data)
        plt.xlabel("symbol of organic compound ")
        plt.ylabel("quantity")
        plt.title(f"Sequence of the {self._type_of_sequence}")
        plt.show()
