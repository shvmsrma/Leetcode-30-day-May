class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count =0;
        Jlist = list(J)
        Slist = list(S)
        for i in range(0,len(Slist)):
            if Slist[i] in Jlist:
                count += 1
            else:
                count = count
        return count 
