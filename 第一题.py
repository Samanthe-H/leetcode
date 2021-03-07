# 1. two sum
# 语言：python
# 第一次提交：（暴力解题）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = 0
        a = False
        for i in range(len(nums)):   
            b = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == b:
                    index2 = j
                    a = True
                    break
            if a == True:
                return [i, index2]
                break
