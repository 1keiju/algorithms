def wiggle_sort(nums):

    """
    Wiggle Sort

    Worst Case: O(nlog(n))
    Worst Case Space: O(n)

    Reference: https://neetcode.io/solutions/wiggle-sort
    """

    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i-1] > nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

if __name__ == "__main__":
    array = [3, 5, 2, 1, 6, 4]

    print(array)
    wiggle_sort(array)
    print(array)


