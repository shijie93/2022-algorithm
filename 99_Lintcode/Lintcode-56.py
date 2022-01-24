class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for index, val in enumerate(numbers):
            if target - val in numbers[index + 1:]:
                return index, numbers[index + 1:].index(target - val) + index + 1



if __name__ == '__main__':
    s = Solution()

    print(s.twoSum([2,7,11,15], 9))