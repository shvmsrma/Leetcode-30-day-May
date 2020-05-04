class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(format(num,"b"))
        comp = binary
        for i in range(0,len(binary)):
            if(binary[i] == '0'):
                comp[i] = '1'
            else:
                comp[i] = '0'
        
        ans =listToStr = ''.join([str(elem) for elem in comp]) 
        return int(ans,2)
