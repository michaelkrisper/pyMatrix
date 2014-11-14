#! /usr/bin/env python3
# coding=utf-8
"""
A simple Matrix class
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-14"


class Matrix:
    def __init__(self, n, m, value=0):
        self.data = [[value for _ in range(n)] for _ in range(m)]
        self.cols = n
        self.rows = m

    @staticmethod
    def zeroes(n, m):
        return Matrix(n, m, 0)

    @staticmethod
    def ones(n, m):
        return Matrix(n, m, 1)

    def __mul__(self, other):
        m = Matrix(self.cols, self.rows)
        m.data = [[cellA * cellB for cellA, cellB in zip(rowA, rowB)] for rowA, rowB in zip(self.data, other.data)]
        return m

    def __add__(self, other):
        m = Matrix(self.cols, self.rows)
        m.data = [[cellA + cellB for cellA, cellB in zip(rowA, rowB)] for rowA, rowB in zip(self.data, other.data)]
        return m

    def __sub__(self, other):
        m = Matrix(self.cols, self.rows)
        m.data = [[cellA - cellB for cellA, cellB in zip(rowA, rowB)] for rowA, rowB in zip(self.data, other.data)]
        return m

    def __eq__(self, other):
        return self.data == other.data and self.rows == other.rows and self.cols == other.cols

    def __str__(self):
        return "\n".join("\t".join(str(cell) for cell in row) for row in self.data)

def main():
    pass


if __name__ == "__main__":
    main()