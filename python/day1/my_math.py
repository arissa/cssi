def sum(nums):
	result = 0
	for n in nums:
		result += n
	return result

def average(nums):
	sum = float(sum(nums))
	return sum/len(nums)


def max(nums):
	max = 0
	for n in nums:
		if n > max:
			max = n
	return n

