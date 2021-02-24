class Solution:
    """
    1，先水平翻转图片，再反转像素值；

    """
    def flipAndInvertImage(self, A: list) -> list:

        # 先进行水平翻转
        for row in A:
            if len(row)<=1:
                break
            left, right = 0, len(row)-1
            while left<right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

        for i, row in enumerate(A):
            row = [1-i for i in row]
            A[i] = row
        return A

A = [
    [1,0,1,0],
    [1,0,1,0]
]
print(Solution().flipAndInvertImage(A))
