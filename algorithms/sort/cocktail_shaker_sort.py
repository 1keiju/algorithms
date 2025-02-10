def cocktail_shaker_sort(arr):

    """
    Cocktail Shaker Sort

    Sorts a given array through a mutation of the bubble sort algorithm.

    Worst Case: O(n^2)
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case Space: O(1)
    
    Reference: https://en.wikipedia.org/wiki/Cocktail_shaker_sort
    """

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
        if swapped == False:
            return arr
        swapped = False
        for i in range(n-1,0,-1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr
