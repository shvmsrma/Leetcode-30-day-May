#Given a positive integer num, write a function which returns True if num is a perfect square else False.

#Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        i = 1
        while(i * i<= num): 
          
        # If (i * i = num) 
            if ((num % i == 0) and (num / i == i)): 
                return True
              
            i = i + 1
        return False    
        
