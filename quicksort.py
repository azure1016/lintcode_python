from median import Solution

so = Solution()
def quickSort(nums,low,high):
    if low < high:
        q = int (low + 1)
        j = so.partition(nums,low,high,q)
        quickSort(nums,low,j-1)
        quickSort(nums,j+1,high)

if __name__ == '__main__':
    nums = [3, 2, 1, 3, 4, 5]
    quickSort(nums,0,len(nums)-1)
    print(nums)