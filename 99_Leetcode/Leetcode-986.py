class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
        输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        '''

        i = j = 0
        ret = []

        while i < len(firstList) and j < len(secondList):

            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            # 不相交
            if a1 > b2 or a2 < b1:
                pass
            else:
                ret.append([max(a1, b1), min(a2, b2)])
            
            if a2 > b2:
                j += 1
            else:
                i += 1
        return ret