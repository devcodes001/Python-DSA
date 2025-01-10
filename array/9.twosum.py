def twosum(nums,target):
	for i in range(len(nums)-1):
		for j in range(1,len(nums)-1):
			if nums[i] + nums[j] :
				return [i,j]
			if len(nums) == 2 and nums[i] == nums[j]:
				return [i,j]

print(twosum(nums =[3,2,3],target =6))
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Start inner loop from i + 1
            if nums[i] + nums[j] == target:
                return [i, j]

print(twosum(nums=[3, 2, 3], target=6))
