# 14. 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        strs type: List[str]
        return type: str
        '''
        # 解法一
        pre = ""
        if not strs: return pre
        for i in range(len(strs[0])):
            if len(strs[0])==0: break
            pre = strs[0][:i+1]
            for s in strs[1:]:
                if(len(s)<i or s[:i+1]!=pre): 
                    return pre[:i]
        return pre

        # 解法二
        if not strs: return ""
        mins = min(strs)
        maxs = max(strs)
        for i,x in enumerate(mins):
            if x!=maxs[i]:
                return mins[:i]
        return mins
