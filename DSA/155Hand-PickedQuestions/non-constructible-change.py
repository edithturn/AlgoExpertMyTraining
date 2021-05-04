def nonConstructibleChange(coins):
    # Sort coins in ascending order
	coins.sort()
    # Define the max_change in zero, this will acumulate the sum of coins
	max_change = 0
	# Iterate all the coins
	for coin in coins:
        # When integers are sorted we can track the high constructible value by doing a acumulative sum
		if coin > max_change + 1:
			break
		max_change += coin
	return max_change + 1
		
coins =[5, 7, 1, 1, 2, 3, 22]
print(nonConstructibleChange(coins))