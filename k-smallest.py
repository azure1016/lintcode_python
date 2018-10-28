import random


class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.select(nums, 0, len(nums) - 1, k)

    def partition(self, A, p, r):
        q = random.randint(p, r)
        pivot = A[q]
        A[q], A[r] = A[r], A[q]
        i = p - 1
        j = p
        for j in range(p, r):
            if A[j] < pivot:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        A[r], A[i + 1] = A[i + 1], A[r]
        return i + 1

    def select(self, A, p, r, k):
        j = self.partition(A, p, r)
        if j == k+p-1:return A[j]
        elif j > k + p - 1:
            return self.select(A, p, j - 1, k)
        else:
            return self.select(A, j + 1, r, k - (j - p + 1))
