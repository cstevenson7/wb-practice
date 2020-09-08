# 1528. Shuffle String
# Add to List
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"

# Input: s = "art", indices = [1,0,2]
# Output: "rat"



# def shuffleString(s, nums):
#     s_list = list(s)
#     for i in range(1,len(nums)):
#         j = i
#         while j > 0 and nums[j] < nums[j-1]:
#             nums[j], nums[j-1] = nums[j-1], nums[j]
#             s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
#             j-=1
#     return ''.join(s_list)

# s = 'art'

# nums = [1,0,2]


# print(shuffleString(s,nums))

# Shuffle String
# Add to List
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"

# Input: s = "art", indices = [1,0,2]
# Output: "rat"

#***************Using two pointer algorithm to find target************

# Problem Statement: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e., the pair) such that they add up to the given target.
# Example: Input: [1, 2, 3, 4, 6], target = 6, Output: [1, 3] (The numbers at index 1 and 3 add up to 6: 2+4=6)


def twoPointers(a_list,target):
    #LIST MUST BE SORTED
    #create pointers for the list below:
    left = 0  # this is our first index
    results = []
    right = len(a_list) -1  # this is the last index 
    while left < right:
        if  a_list[left]  + a_list[right] > target:
            right -= 1
        elif a_list[left]  + a_list[right] < target:
            left +=1 
        else:
            results.append(left)            
            results.append(right)      
            return results

target = 12
my_list2 = [1,5,8,11,13,42]
print(twoPointers(my_list2,target))











# Sample Problem for Two Pointers: Pair with the target sum
# Problem Statement: Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e., the pair) such that they add up to the given target.


