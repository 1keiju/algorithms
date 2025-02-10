import random

def bogo_sort(arr, simulation=False):
    
    """
    Bogo Sort
    
    Bogo sort is a very inefficient sorting algorithm that uses random.shuffle.
    It will randomly sort, then see if the array is in the proper order.

    Worst Case: O(∞)
    Best Case: O(n)
    Average Case: O(n * n!)
    Worst Case Space: O(1)

    Reference: https://en.wikipedia.org/wiki/Bogosort
    """
    
    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
    
    def is_sorted(arr):
        
        #check that the array is in order
        i = 0
        arr_len = len(arr)
        while i+1 < arr_len:
            if arr[i] > arr[i+1]:
                return False
            i += 1
        return True
    
    while not is_sorted(arr):
        random.shuffle(arr)
        
        if simulation:
            iteration = iteration + 1
            print("iteration",iteration,":",*arr)
            
    return arr
