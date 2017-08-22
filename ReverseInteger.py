class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        else:   
            x = str(x)
            if '-' in x:
                print ("111")
                x=int('-'+''.join(reversed(x[1::])))
            else:
                print ("222")
                x = reversed(x)
                x=int(''.join(x))
            if abs(x) > 2**31:
                print ("333")
                return 0
            else:
                print ("444")
                return x 
# print (Solution().reverse(-1123))
# x = str(-123)
# print (''.join(reversed(x[::-1])))
print (10 %10)