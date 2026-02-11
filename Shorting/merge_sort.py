# https://www.geeksforgeeks.org/problems/merge-sort/1

class Solution:
    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            # Sort left half
            self.mergeSort(arr, l, mid)
            # Sort right half
            self.mergeSort(arr, mid + 1, r)
            # Merge the two halves
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        # Create temporary arrays
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]

        i = j = 0
        k = l

        # Merge back into arr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1