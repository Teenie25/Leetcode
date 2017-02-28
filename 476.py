class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=0
        bef=num
        while num>0:
            num=num>>1
            i=i+1
        sum=pow(2,i)-1
        #print num
        complement=sum-bef
        return complement
                
       
            
        
        
        
