#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = list(s)
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        unique=[]    
        for k,v in freq.items():
            if(v==1):
                unique.append(k)
        indexs=[]
        for x in unique:
            indexs.append(l.index(x))
       
        if(len(indexs)>0):
            
            return min(indexs)
        else:
            return -1
                
