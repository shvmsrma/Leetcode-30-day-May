# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
         return self.bs(0,n)

    def bs(self,s,e):
        if e==s:
            return e
        mid=s+ (e-s)//2
        cur=isBadVersion(mid)    
        if cur==True:
            return self.bs(s,mid)
        if cur==False:
            return self.bs(mid+1,e)
