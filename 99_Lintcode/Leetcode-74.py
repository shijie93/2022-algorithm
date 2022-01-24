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

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))