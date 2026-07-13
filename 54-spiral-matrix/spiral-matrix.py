class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        result = []

        while top <= bottom and left <= right:

            # Left -> Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Top -> Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right -> Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Bottom -> Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result