def selection_sort(arr, simulation=False):

    """
    Selection Sort

    Worst Case: O(n^2) comparions, O(n) swaps
    Best Case: O(n^2) comparions, O(1) swaps
    Average Case: O(n^2) comparions, O(n) swaps
    Worst Case Space: O(1)

    Reference: https://en.wikipedia.org/wiki/Selection_sort
    """

    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # "Select" the correct value
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
        
        if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)
            
    return arr
