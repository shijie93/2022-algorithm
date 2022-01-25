class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        hight = len(matrix) - 1

        i= 0
        while i < hight:

            if matrix[i][0] <= target < matrix[i + 1][0]:
                if target in matrix[i]:
                    return True
                else:
                    return False
            i += 1
        
        return target in matrix[hight]

    def searchMatrix_2(self, matrix, target) -> bool:
        ''' 二分法 '''

        heigh = len(matrix)
        if heigh == 0:
            return False

        width = len(matrix[0])

        left = 0
        right = heigh * width - 1

        while left <= right:

            mid = (left + right) // 2
            i = mid // width
            j = mid % width

            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix_2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))