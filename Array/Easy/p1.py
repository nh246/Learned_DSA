#https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0

class Solution:
    def largest(self, arr):
        # code here
        temp = arr[0]
        for i in arr:
            if i > temp:
                temp = i
        return temp