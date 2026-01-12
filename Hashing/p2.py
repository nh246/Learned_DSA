# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

class Solution:
    def frequencyCount(self, arr):
        #  code here
        n= len(arr)
        result = [0]*n
        for val in arr:
            result[val-1]+=1
        return result
           