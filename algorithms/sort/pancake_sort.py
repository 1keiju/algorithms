def pancake_sort(arr):
    """
    Pancake Sort

    Sorts a given array using a mutation of the selection sort algorithm.

    Overall Time Complexity: O(n^2)

    Reference: https://www.geeksforgeeks.org/pancake-sorting/
    """

    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    for cur in range(len(arr), 1, -1):
        #Finding index of maximum number in arr
        index_max = arr.index(max(arr[0:cur]))
        if index_max+1 != cur:
            #Needs moving
            if index_max != 0:
                #reverse from 0 to index_max
                arr[:index_max+1] = reversed(arr[:index_max+1])
            # Reverse list
            arr[:cur] = reversed(arr[:cur])
    return arr
