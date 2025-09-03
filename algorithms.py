#Duplicate Values

def no_duplicate(nums):
    if len(set(nums)) == len(nums):
        return True
    else:
        return False
    

#Given an array nums containing n distinct numbers in the range [0, n] 
# return the only number in the range that is missing from the array
# example => [3,0,1] == returns 2

def missing_number(nums):
    n = len(nums)
    sum = n*(n+1) / 2
    total = sum(nums)
    return sum - total

# 28 min https://www.youtube.com/watch?v=lvO88XxNAzs


# Two sum


def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num], i]
        else:
            hash_map[num] = i




