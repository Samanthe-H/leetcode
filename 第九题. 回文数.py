# 9. isPalindrome
class Solution:
    def reverse(x: int):
        x_re = 0
        while x!=0:
            x_re = x%10 + x_re*10
            x = x//10
        return x_re
    
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): return False
        else:
            if(x>0 and x%10 ==0): return False
            else:
                y = Solution.reverse(x)
                if y==x : return True
                else: return False

        # if x==0: return True
        # elif(x>=0 and x%10!=0): 
        #     if Solution.reverse(x)==x : return True
        #     else: return False
        # else: return False
