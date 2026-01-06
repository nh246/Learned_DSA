# https://www.geeksforgeeks.org/problems/palindrome-string0817/1

class Solution:
    def isPalindrome(self, s):
        # code here
        l = 0
        r = len(s) -1
        
        def final(l ,r):
            if(l>=r):
                return True
            if (s[l] != s[r]):
                return False
            return final(l+1 , r-1)
        return final(l,r)