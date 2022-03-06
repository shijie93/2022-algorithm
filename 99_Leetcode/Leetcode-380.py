import random
class RandomizedSet:

    def __init__(self):
        # 数组存放数据
        self.nums = []

        # 构建字典 {value: index from nums}
        self.valToIndex = dict()


    def insert(self, val: int) -> bool:
        # 如果已存在，直接返回False
        if val in self.valToIndex:
            return False
        
        # 记录 {v:i} 并追加，返回 True
        self.valToIndex[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
        if val not in self.valToIndex:
            return False
        # 如果存在，则保存 nums 最后一个数的坐标到待删除的坐标，然后删除最后一个
        # 将最后一个数的坐标更新为待删除的坐标
        self.valToIndex[self.nums[-1]] = self.valToIndex[val]
        self.nums[self.valToIndex[val]], self.nums[-1] = self.nums[-1], self.nums[self.valToIndex[val]]
        # 删除 val 和 nums 中的相关内容
        self.valToIndex.pop(val)
        self.nums.pop()
        return True


    def getRandom(self) -> int:
        return self.nums[random.choice(range(len(self.nums)))]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()