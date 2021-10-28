def twoNumberSum(array, targetSum):
	twosumres = {}
	
	for i, num in enumerate(array):
		complement = targetSum - num
		if complement not in twosumres:
			twosumres[num] = i
		else:
			return [complement, num]
		
	return []