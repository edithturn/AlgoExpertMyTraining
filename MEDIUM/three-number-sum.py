def threeNumberSum(array, targetSum):
    """
    Using 02 pointer and complement of sum to get the two remaining numbers. If the sum of both numbers is less than temporal sum(tem_sum)
    increate left pointer in one, if sum of bot numbers is grather than temporal sum, decrese in one right pointer.
    Time    : O(n^2)
    Space   : O(n)
    """
    def threeNumberSum(array, targetSum):
        # Write your code here.
        array = sorted(array)
        res = []
        for i in range(len(array)):
            left = i + 1
            right = len(array) - 1
            tmp_sum = targetSum - array[i]
            while(left < right):
                if array[left] + array[right] == tmp_sum:
                    res.append([array[i], array[left], array[right]])
                    left  += 1
                    right -= 1
                elif array[left] + array[right] < tmp_sum:
                    left += 1
                else:
                    right -= 1
        return res
			
			