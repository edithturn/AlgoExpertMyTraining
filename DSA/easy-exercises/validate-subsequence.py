def isValidSubsequence(array, sequence):
    """
    using a counter which will increase in one if a number in the array is equal a number in sequence.
    Time: O(n)
    Space: O(1)
    """
    count = 0
    for num in array:
        if num == sequence[count]:
            count += 1
        if count == len(sequence):
            return True
    return False


array = [5, 1,23,6, 25,-1,7,10]
sequence = [1,6,-1,10]
print(isValidSubsequence(array, sequence))


array1 = [1, 6]
sequence1 = [1,6,-1,10]
print(isValidSubsequence(array1, sequence1))