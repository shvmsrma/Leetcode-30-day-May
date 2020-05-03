class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r= list(ransomNote)
        m =list(magazine)
        count = 0
        for x in r:
            if x in m:
                count +=1
                m.remove(x)
            else:
                count = count
        
        if(count == len(r)):
            return True
        else:
            return False
