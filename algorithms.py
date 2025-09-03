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



#given the array nums for each nums[i] find out how many numbers in the array are smaller than it
#that is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i]
#return the answer in an array
#Example => Input: nums = [8,1,2,2,3] Output: [4,0,1,1,3]


def small_number(nums):
    smallnum = []

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            
            if nums[i] != nums[j] and nums[i] > nums[j]:
                count +=1
        smallnum.append(count)
            
    return smallnum
    
nums = [8,1,2,2,3]
print(small_number(nums))


#another way
def rank(nums):
    ranks = {}
    for i, n in enumerate(nums):
        if n not in ranks:
            ranks[n] = i 
    return ranks
    

def small_number(nums):
    sortednums = sorted(nums)
    ranks = rank(sortednums)
    smaller = [ranks[num] for num in nums]
    return smaller
    
nums = [8,1,2,2,3]
print(small_number(nums))

#Minimum time visiting all points
#On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi].Return the minimum time in seconds to visit all points in the order given by points.
#You can move according to the next rules:  
#In 1 second, you can either:
#move vertically by one unit,   
#move horizontally by one unit, or
#move diagonally (it means to move one unit vertically and one unit horizontally in 1 second).
#You have to visit the points in the same order as they appear in the array. You are allowed to pass through points that appear later in the order, but these do not count as visits.
#Example => Input: points = [[1,1],[3,4],[-1,0]] Output: 7


def min_time(points):
    time = 0
    x1,y1 = points.pop()
    while points:
        x2,y2 = points.pop()
        dist = max(abs(x2-x1), abs(y2-y1))
        time += dist
        x1,y1 = x2,y2
    return time
    

pints = [[1,1],[3,4],[-1,0]]
print(min_time(pints))