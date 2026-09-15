class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l_ptr = 0
        r_ptr = t - 1

        while l_ptr <= r_ptr:
            m = (l_ptr + r_ptr) // 2
            i = m // n
            j = m % n

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r_ptr = m - 1
            else:
                l_ptr = m + 1

        return False