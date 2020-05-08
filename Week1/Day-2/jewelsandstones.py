#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
#Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#The letters in J are guaranteed distinct, and all characters in J and S are letters.
#Letters are case sensitive, so "a" is considered a different type of stone from "A".

#Solution : 

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
