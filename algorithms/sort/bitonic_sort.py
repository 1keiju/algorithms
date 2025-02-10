def bitonic_sort(arr, reverse=False):

    """
    Bitonic Sort

    Bitonic sort is a sorting algorithm that can be parallelized; however, this code does not contain that.
    This code can only sort an array whos size is a power of 2.
    Sorting in increasing or decreasing order can be toggled by the reverse argument. (true = increasing)
    
    Worst Case: O(log(n)^2)
    Best Case: O(log(n)^2)
    Average Case: O(log(n)^2)
    Worst Case Space: O(nlog(n)^2)
    
    Reference: https://en.wikipedia.org/wiki/Bitonic_sorter
    """
    
    def compare(arr, reverse):
        n = len(arr)//2
        for i in range(n):
            if reverse != (arr[i] > arr[i+n]):
                arr[i], arr[i+n] = arr[i+n], arr[i]
        return arr

    def bitonic_merge(arr, reverse):
        n = len(arr)
        
        if n <= 1:
            return arr
        
        arr = compare(arr, reverse)
        left = bitonic_merge(arr[:n // 2], reverse)
        right = bitonic_merge(arr[n // 2:], reverse)
        return left + right
    
    # end of function (compare and bitionic_merge) definition
    n = len(arr)
    if n <= 1:
        return arr
    
    # checks if n is a power of two
    if not (n and (not(n & (n - 1))) ):
        raise ValueError("the size of input should be power of two")
    
    left = bitonic_sort(arr[:n // 2], True)
    right = bitonic_sort(arr[n // 2:], False)

    arr = bitonic_merge(left + right, reverse)
        
    return arr
