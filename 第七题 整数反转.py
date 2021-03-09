# 7.整数反转
# 初始提交：
class Solution:
    def reverse(self, x):
        '''
        type x: int
        rtype : int
        '''
        x_re = 0
        sign_p = 1
        if(x != 0):
            if(x < 0): 
                sign_p = -1
                x = abs(x)
            while(x!=0):
                x_re = x_re*10 + x % 10
                x = x//10
            if(x_re>(2**31)-1 or x_re < -2**31):
                return 0
        return sign_p*x_re
# 评分：	36 ms	14.9 MB
        
# 修改1：
class Solution:
    def reverse(self, x):
        '''
        type x: int
        rtype : int
        '''
        x_re = 0
        y = abs(x)
        if(x != 0):
            while(y!=0):
                x_re = x_re*10 + y % 10
                y = y//10
            if(x_re>(2**31)-1 or x_re < -2**31):
                return 0
        if x>=0: return x_re
        else: return -x_re
# 评分：	40 ms	14.9 MB

# 修改2：
class Solution:
    def reverse(self, x):
        '''
        type x: int
        rtype : int
        '''
        x_re = 0
        y = abs(x)
        while y!=0:
            x_re = y%10 + x_re*10
            if(x_re>(2**31)-1 or x_re < -2**31): return 0
            y = y//10
        if x>=0: return x_re
        else: return -x_re
# 评分：	28 ms	15 MB
