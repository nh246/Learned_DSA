# https://www.geeksforgeeks.org/problems/insertion-sort/0

class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):  # start from second element
            key = arr[i]
            j = i - 1
            # shift elements greater than key to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key  # place key in correct position