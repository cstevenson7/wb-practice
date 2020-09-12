# # Brians Practice interview question with me - Spet 8, 2020
# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

# Example 1:
# Input: [1,2,2,1,3,1]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
# No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true 

# Constraints:
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

# class Solution:
def occurences(array):
    num_dict = {}
    for i in range(0,len(array)):
        if array[i] not in num_dict:
            num_dict[array[i]] = 1
        else:
            num_dict[array[i]] +=1
    num_list = []
    for value in num_dict.values():
        if value not in num_list:
            num_list.append(value)
        else:
            return False
    return True

array = [-3,0,1,-3,1,1,1,-3,10,0]
print(occurences(array))










