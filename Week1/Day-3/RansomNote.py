#Given an arbitrary ransom note string and another string containing letters from all the magazines,
#write a function that will return true if the ransom note can be constructed from the magazines ; 
#otherwise, it will return false.
#Each letter in the magazine string can only be used once in your ransom note.

#Solution:

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
