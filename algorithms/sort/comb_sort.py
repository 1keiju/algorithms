def comb_sort(arr):

    """
    Comb Sort

    Essentially an improved version of the bubble sort alogrithm.

    Worst Case: O(n^2)
    Best Case: O(n*log(n))
    Average Case: O((n^2)/2^p), p = number of increments
    Worst Case Space: O(1)

    Reference: https://en.wikipedia.org/wiki/Comb_sort
    """
    
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                sorted = False
            i = i + 1
    return arr
