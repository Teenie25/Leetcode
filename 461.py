class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res=x^y
        count=0
        i=0
        for i in range(0,32):
            if res&1:
                count=count+1
            res=res>>1
        return count
