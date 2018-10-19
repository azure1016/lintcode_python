import random


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A):
        # write your code here
        self.quickSort(A, 0, len(A) - 1)

    def quickSort(self, A, p, r):
        if p < r:
            q = random.randint(p, r)
            j = self.partition(A, p, r, q)
            self.quickSort(A, p, j - 1)
            self.quickSort(A, j + 1, r)

    def partition(self, A, p, r, q):
        pivot = A[q]
        A[q], A[r] = A[r], A[q]
        i = p - 1
        j = p
        while j < r:
            if A[j] <= pivot:
                i = i + 1
                A[j], A[i] = A[i], A[j]
            j = j + 1
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1


if __name__ == '__main__':
    A = [19,-10,-2,40,3,36,57,25,66,51,5,40,-8,43,9,-5,0,4,55,28,63,67,-2,35,57,0,0,30,17,55,22,34,-4,42,57,52,4,65,6,-2,8,12,31,43,26,34,31,19,-3,36,34,11,58,23,13,7,17,10,33,-5,10,53,14,56,18,8,-6,-2,37,7]
    B = [1, 3, 3, 3, 1]
    s = Solution()
    s.sortIntegers2(A)
    print(A)