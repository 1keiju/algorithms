def shell_sort(arr):

    """
    Shell Sort

    Worst Case: O(n^2)
    Best Case: O(nlog(n))
    Worst Case Space: O(n)

    Reference: https://en.wikipedia.org/wiki/Shellsort
    """

    n = len(arr)
    # Initialize size of the gap
    gap = n//2
    
    while gap > 0:
        y_index = gap
        while y_index < len(arr):
            y = arr[y_index]
            x_index = y_index - gap
            while x_index >= 0 and y < arr[x_index]:
                arr[x_index + gap] = arr[x_index]
                x_index = x_index - gap
            arr[x_index + gap] = y
            y_index = y_index + 1
        gap = gap//2
        
    return arr
