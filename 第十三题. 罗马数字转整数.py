# 13. romanToInt

class Solution:
    def inromanToInt(string):
        if string=="I": return 1
        elif string=="V": return 5
        elif string=="X": return 10
        elif string=="L": return 50
        elif string=="C": return 100
        elif string=="D": return 500
        else: return 1000
    
    def romanToInt(self, s):
        '''
        type s:str
        rtype: int 
        '''
        value = []
        for index,string in enumerate(s):
            value.append(Solution.inromanToInt(string))
            if(value[index]>value[index-1]):
                temp = value[index]-value[index-1]
                value[index] = temp
                value[index-1] = 0
        return sum(value)
