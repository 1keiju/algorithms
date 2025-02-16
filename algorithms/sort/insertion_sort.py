def insertion_sort(arr, simulation=False):

    """
    Insertion Sort

    Worst Case: O(n^2)
    Best Case: O(n) comparisons, O(1) swaps
    Average Case: O(n^2)
    Worst Case Space: O(n)

    Reference: https://en.wikipedia.org/wiki/Insertion_sort
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)

    return arr
