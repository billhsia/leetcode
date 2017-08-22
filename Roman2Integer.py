class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #重點在於 羅馬數字特性 右邊大於左邊數字時 是減 左邊大於右邊數字是加 最後一個數字運算一定為加
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        sum = 0
        for i in range(0, len(s)-1):
        	if roman[s[i]] < roman[s[i+1]]:
        		sum -=roman[s[i]]
        	else:
        		sum+=roman[s[i]]
        return sum+roman[s[-1]]
print (Solution().romanToInt("XV"))