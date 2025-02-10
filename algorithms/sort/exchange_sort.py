def exchange_sort(arr):

    """
    Exchange Sort
    
    Worst Case: O(n^2)
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case Space: O(1)
    
    Reference: https://sortingalgos.miraheze.org/wiki/Exchange_Sort
    """

    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(i+1, arr_len):
            if(arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr
