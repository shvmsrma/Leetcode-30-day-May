#You are a product manager and currently leading a team to develop a new product. 
#Unfortunately, the latest version of your product fails the quality check. 
#Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
#which causes all the following ones to be bad.
#You are given an API bool isBadVersion(version) which will return whether version is bad. 
#Implement a function to find the first bad version. You should minimize the number of calls to the API



# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#Solution:

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
