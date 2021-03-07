# 1. two sum
# 语言：python3
# 初始提交：（暴力解题）
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
# 评分：44 ms  15 MB 或者 40ms 14.9MB.
               
# 优化1：方法不变，变量减少
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens):   
            b = target - nums[i]
            for j in range(i+1,lens):
                if nums[j] == b:
                    return [i, j]
# 时间不变，44 ms  14.9 MB,占用内存减少.

# 优化2：使用字典+枚举 + 界面美化
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if num2 in map:
                return [map[num2],index]
            map[num1] = index
# 评分：40 ms	14.7 MB

# 优化3：使用字典中的dict.__contains__(key)判断键是否存在
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, num1 in enumerate(nums):
            num2 = target - num1
            if map.__contains__(num2):
                return [map[num2],index]
            map[num1] = index
