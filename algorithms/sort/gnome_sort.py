def gnome_sort(arr):

    """
    Gnome Sort

    Worst Case: O(n^2)
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case Space: O(1)

    Reference: https://en.wikipedia.org/wiki/Gnome_sort
    """

    n = len(arr)
    index = 0
    while index < n:
        if index == 0 or arr[index] >= arr[index-1]:
            index = index + 1
        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index = index - 1
    return arr
