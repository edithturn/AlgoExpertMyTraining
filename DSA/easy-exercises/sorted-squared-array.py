def sortedSquaredArray(array):
    """
    Add the square of each element in the array into the second array. Considering positives.
    Time  O(n), iterating each element once
    Space O(n), using another array to storage square of the firts array
    """
    result = []

    for i in array:
        if i < 0 :
            i = i*(-1)
        result.append(i*i)
    result.sort()
    return result
  
nums = [1,2,3,5,6,8,9]
print(sortedSquaredArray(nums))