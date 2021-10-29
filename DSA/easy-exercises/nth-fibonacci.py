def getNthFib(n):
    """
    Recursive function to get the the fibonacci number, if n is two return 1,
    if n is one, return 0.
    Time    : O(2^n)
    Space   : O(n) , recursion use stack to storage values.
    """
    if n == 2:
        return 1
    elif n == 1:
        return 0
    return getNthFib(n-1) + getNthFib(n-2)

# Dry Run

#                 6
#             /       \
#          5            4
#        /   \        /   \
#      4      3      3      2  
#     / \    / \    / \    / \
#    3   2  2   1  2   1  1   0
#   /  \
#  2    1

print(getNthFib(6)) # 6
print(getNthFib(5)) # 3
print(getNthFib(2)) # 1

# 6
# 5 // 0,1,1,2,3,5