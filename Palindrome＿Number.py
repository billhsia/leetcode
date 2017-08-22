class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ＃技巧在於將左右兩邊的數字做對比後 將左右兩個數排除繼續對比直到結束 過程中有不一致就回傳False
        if x <0:
        	return False
        digit=1
        while x//digit >=10:
        	digit *=10
        while x:
        	left = x//digit
        	right= x%1
        	if left!=right:
        		return False       	
        	x = (x%digit)//10
        	digit//=100
        return True
print (Solution().isPalindrome(1331))
