def bubble_sort(arr, simulation=False):

    """
    Bubble Sort

    If bubble_sort(arr,True) is called, the process of the sort will be shown.
    The default setting is simulation = false.

    Worst Case: O(n^2)
    Best Case: O(n) comparisons, O(1) swaps
    Average Case: O(n^2)
    Worst Case Space: O(n)

    Reference: https://en.wikipedia.org/wiki/Bubble_sort
    """

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                if simulation:
                    iteration = iteration + 1
                    print("iteration",iteration,":",*arr)
                    
    return arr
