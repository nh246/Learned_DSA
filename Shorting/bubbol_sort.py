# https://www.geeksforgeeks.org/problems/bubble-sort/1


class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n):
            swp= False
            for j in range(0 ,n-i-1):
                if arr[j] > arr[j+1]:
                   arr[j],arr[j+1]=arr[j+1],arr[j]
                   swp= True
            if not swp:
                break
        return arr