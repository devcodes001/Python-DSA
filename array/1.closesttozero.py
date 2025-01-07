# Problem : https://leetcode.com/problems/find-closest-number-to-zero/description/

def closest_to_zero(nums):
	closest = nums[0]
	for i in nums:
		if abs(i) < closest:
			closest = i
	if closest < abs(closest):
		return abs(closest)
	else:
		return closest
print(closest_to_zero([2,-1,1]))