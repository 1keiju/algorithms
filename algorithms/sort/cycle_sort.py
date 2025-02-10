def cycle_sort(arr):

    """
    Cycle Sort

    Permutations are decomposed into cycles, which are then indiviually rotated, providing the result.

    Worst Case: O(n^2)
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case Space: O(n)

    Reference: https://en.wikipedia.org/wiki/Cycle_sort
    """

    # helper function for finding where to put a key
    def cycle_sort_helper(arr, start, key):

        index = start
        for i in range(start+1, len(arr)):

            # caluclate index to place key
            if arr[i]<key:
                index += 1

        return index

    # going through array
    for start in range(len(arr)-1):

        # call helper to find where to place the key
        key = arr[start]
        location = cycle_sort_helper(arr, start, key)

        # when equivalent, go to next iteration
        if location == start:
            continue

        # place key in location
        while key == arr[location]:

            # increment location to deal with cases of same number
            location += 1

        # placing
        temp = arr[location]
        arr[location] = key
        key = temp

        # rotate cycle
        while location != start:

            # call helper to find where to place the key
            location = cycle_sort_helper(arr, start, key)

            # place key in location
            while key == arr[location]:

                # increment location to deal with cases of same number
                location += 1

            # placing
            temp = arr[location]
            arr[location] = key
            key = temp

    return arr

# simple test case
if __name__ == "__main__":
    test_array = [1, 7, 4, 8, 13, 15]
    print(test_array)
    cycle_sort(test_array)
    print(test_array)