# https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1

#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		left = l -1
		right = r-1
		def final(arr,left,right):
		    if(left>=right):
		        return
		    arr[left],arr[right]=arr[right],arr[left]
		    
		    final(arr,left+1,right-1)
		final(arr, left, right)

	    return arr