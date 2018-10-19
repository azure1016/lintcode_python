import random


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        low = 0
        high = len(nums) - 1
        kth = int(len(nums) / 2) + 1
        return self.select(nums, low, high, kth)

    def partition(self, nums, low, high, q):
        i = low - 1
        j = low
        pivot = nums[q]
        nums[q], nums[high] = nums[high], nums[q]
        while j <= high:
            if nums[j] < pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
            j = j + 1
        nums[high], nums[i+1] = nums[i+1], nums[high]
        res = i+1
        return res

    def select(self, A, low, high, k):
        q = random.randint(low, high)
        j = self.partition(A, low, high, q)
        if j == low + k - 1: return A[j]
        if j > low + k - 1:
            return self.select(A, low, j - 1, k)
        else:
            return self.select(A, j + 1, high, k - (j - low + 1))


if  __name__ == '__main__':
    so = Solution()
    A = [7,9,4,5]
    print(so.median(A))