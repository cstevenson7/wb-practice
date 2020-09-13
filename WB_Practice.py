
##w2 day2******Given a number as an input, print "Fizz" if the number is even,
#  "Buzz" if the number is odd.#



#w2 day3**************Given a string as a parameter to a function,
#  return True if the string is a palindrome and False if not






##w2day4******Find all the even numbers for a list and put them in a new list
#Questions - the lists just have numbers, and all integers, and no zero

# def find_evens(list):
#     evens = []
#     for num in numbers



# numbers= [3,9,2,11,4,6]


#**********Week3 Day1 # Remove Element
# Given a list of numbers and a value as input to a function, remove all instances of that value "in-place" and return the new length of the list
# Input: nums = [3,2,2,3] 
# Output: return a length == 2

# def remove_element(numbers, target):
#     #a_list = []
#     for num in numbers:
#         if num == target:
#             numbers.remove(target)
#     return len(numbers)

# target = 3
# numbers = [3,4,6,3,3]
# print(remove_element(numbers, target))

# def remove_element(nums,target):
#     print(len(nums))
#     for num in nums:
#         if target == num:
#             nums.remove(target)
#     return len(nums)

# target = 3
# nums = [3,2,2,35,3,7,-3]
# print(remove_element(nums, target))






# #******************week3 day2 - Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “),
# return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.

# Example Input: “Hello World”
# Example Output: 5
# Example Input 2: “The brown loud cow plowed”
# Example Output 2: 6

# def last_word(s):

#     word_list = s.split()
#     last_word = word_list[-1]
#     return len(last_word)

# s = 'The brown loud cow plowed'
# print(last_word(s))




#*******************week3 day3 remove vowels
# Create a function that given a string remove the vowels in the string and return the string.
# Example Input: “Joel”
# Example Output: “Jl”

# def remove_v(s):
#     vowels = 'aeiou'
#     for char in s:
#         if char in vowels:
#             s = s.replace(char,"")
#     return s


# s = 'Cindy'
# print(remove_v(s))


        








#*********************Binary Search Practice
#Big O notation is O(log(n))
#                                                               








#******************Week3-day4- WB Question

# FInd smallest number  - (Without min)
# Create a function that given a list of numbers (non-sorted) find the lowest number in the list and return it.
# Example Input: [50,30,4,2,11,0]
# Example Output: 0
# Example Input 2: [40,3,4,2]
# Example Output 2: 2


##ALWAYS GO WITH THE BEST WORKING SOLUTION THAT MAKES SENSE TO USAE THEN 
# REFACTOR TO MAYBE AN ALGORITHM. HAVING A SOLUTION IS BETTER THAN MOVE

# time and space complexity this is constant space , time with .sort() is
#  because we have to add another operation for sorting we out in the logn timre 
# __builtin__ methods take some time  more like because sort() is a hybrid sorting function
#   - this is the solution  but it moves it to a log n amount of time  merge sort would be better
# but overkill for this

#talking about this because of potential interview questions

#f you can't use sort mothod, change the list to a dictionat and use . lowest()  function??because dictionarty run in >>time ,
#  but here you need more space #because you create a dictionary

# def lowest(numbers):
#    numbers.sort()
#    lowest = numbers[0]
#    return lowest

# numbers = [40,3,4,2]
# print(lowest(numbers))

# #helper Function
# def swap( i,j, array):
#     array[i], array[j] = array[j] , array[i]

# def insertSort(array):
#     for i in range(1,len(array)): #We start at the secone value in the array index 1
#         j = i  # j is a placeholder for i ( the next values in the list) to keep track of where we are in the array
#         # if then number behind [j], is less than [j] .. swap them
#         while j > 0 and array[j] < array[j-1]:
#             swap(j ,j-1, array)
#             j -= 1  # look at the num behind j 
#     return array

# print(insertSort([30,2,1]))


# def swap( i,j, array):
#     array[i], array[j] = array[j] , array[i]

#Insertion sort to find lowest, to find highest swap the > sign, duh 
# def lowest(numbers):
#     for i in range(1,len(numbers)):
#         j=i
#         while j > 0 and numbers[j] < numbers[j-1]:
#             #swap(j ,j-1, numbers)
#             numbers[j], numbers[j-1] = numbers[j-1] , numbers[j]
#             j -=1   # this stop the while loop so we can get the next i in the outer loop until we have gone thru the list once
#     return numbers[0]

# numbers = [40,3,4,2]

# print(lowest(numbers))







#***********good dictionary/string/list problem from week3-day3 Exercise 2
### Exercise #2 <br>
#Create a function that counts how many distinct words are in the string below.
#Then outputs a dictionary with the words as the key and the value as the amount of times
#that word appears in the string.<br>



# import re

# def distinctWords(a_text):
#     str1 = re.sub(r'[,.:@#?!&$]','', a_text) # this removes all punctuation in a string
#     word_dict={}
#     word_list = []
#     word_list = str1.lower().split()
#     for word in word_list:
#         if word not in word_dict:
#             word_dict[word] = 1
#         else:
#             word_dict[word] +=1
#     return word_dict



# a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# print(distinctWords(a_text))




#****************** my question1 **************
# # print out the index of each letter of a string
#enumerate(iterable, start) 	A Number. Defining the start number of the enumerate object.  Default 0
# str1 = "Cindy"
# for index,char in enumerate(str1, start = 1):
#     print(index , char)




 #*************   my Question2**************
 # print out the value and each index of a list

# def printList(a_list):
#     for i in range(len(a_list)):
#         print(f" The index {i} value is {a_list[i]}")
#     inset_arr = a_list[1]
#     print(inset_arr)
#     print(a_list[1][1])

# a_list= ['one',['cherry', 'horse'], 'shoe']


# printList(a_list)



	
#********************myQuestion3******************

# For a given number num, write a function to test if it's a numerical palindrome or not and
#  return a boolean (true if it is and false if not).
# Return "Not valid" if the input is not an integer or less than 0.
#MY NOTE Don't have ot check each number , just the actual number if it is not a int or negative



    





#************************** recursive factorial function Week3-day2***************
# this is 5! = 5 * 4 * 3 * 2 * 1

#This starts at 5, then goes down the stack  until 1(or2?) then starts multiplying the values to itself up the stack
#  1 *1 = 1  1*2 = 2  2*3 = 6  6*4 = 24 24*5 = 120   5 is the number we passed to the function
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
     





#******************* Recursive fibonnaci functionWeek3 -day2*********************

 



#***************** In-Place or swap Week3day3 ****************

# def swap(array, i,j,k ):

#     array[i], array[j], array[k] = array[k],array[j], array[i]
#     return array

# array = [56,89,2, 99,80,5]
# print(swap(array,1,2,3))




#***************** TwoPointers Week3day3 ****************





#***************WB Week3 Day1 -Non repeating characters

# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1.
# Examples:
# Input - s = "leetcode"
# Output - return 0
# Input - s = "loveleetcode"
# Output - return 2
#  'aaa' return  -1


# def firstUniqChar(s):
#     letter_dict = {}
#     # for each letter in the string if it is not in the dictionary add it
#     # and the count will be one. The key for the dict is the string letter
#     #and the values is the frequency of the letter
#     for char in s:
#         if char not in letter_dict:
#             letter_dict[char] = 1
#         else:
#             # if it is in the dictionay add one to the exiting letter coint
#             letter_dict[char] += 1
#     #loop throught the dictionary annd find the first non repeating letter(the count or value)will be one      
#     for char in s:
#         #want the  Key of the first letter in the string that has a count of 1
#         # return that index of the string for that letter
#         if letter_dict[char] == 1:
#             return s.index(char) # the return is like a break, it stops the for loop
#                                   #one this is found we are done
#     # here the forloop has gone through all the letters in the string and no letter had a frequency of one
#     #  so there are no unique letters
#     return -1


# print(firstUniqChar('lllll'))   

#******************WB Question Week4 day2

# WB Question wk3 day3

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

#mine works
# import re
# # def palindrome(str1):
# #     str2 = re.sub(r'[,.:@#?!&$]', '',str1)
# #     str2 = str2.replace(" ", "")
# #     str2 = str2.lower()
# #     if str2 == str2[::-1]:
# #         return True

# #     else:
# #          return False
    
# # str1 = "race a car"
# # str2 = "A man, a plan, a canal: Panama"
# # print(palindrome(str1))

# #Brians  one liner

# def isPal(s):
#     s_as_lst = [x.lower() for x in s if x.isalnum()]
#     return s_as_lst == s_as_lst[::-1]
        
# str1 = "race a car"
# str2 = "A man, a plan, a canal: Panama"

# print(isPal(str2))




#*******************************week4 day3 WB

# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21

# def rev_digit(n):
#     neg = ''
#     if n < 0:
#         neg = 'y'
#         n = abs(n)
    
#     n_str = str(n)
#     n_str = n_str[::-1]
#     new_n = int(n_str)

#     if neg =='y':
#         new_n *= -1
#         return new_n
#     else:
#         return new_n

# n = 120
# print(rev_digit(n))








#****************************week4 day4 
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# five = ListNode(5)
# four = ListNode(4, five)
# three = ListNode(3, four)
# two = ListNode(2, three)
# one = ListNode(1, two)
# def reverseList(head):
#   class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# five = ListNode(5)
# four = ListNode(4, five)
# three = ListNode(3, four)
# two = ListNode(2, three)
# one = ListNode(1, two)

# def reverseList(head):
#     current = head
#     prevoius = None 
    
#     while current:
#         temp = current        
#         current = current.next # point2
#         temp.next = prevoius
#         prevoius = temp
#     return temp    
    
# print(reverseList(one))

###***************************Week4 day5**************************
# 1365. How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.
 
# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

 # Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100
# def how_many_smaller(nums):    
#     result_list = []
#     for num in nums: # both loops use the same list/array
#         count = 0
#         for j in nums:
#             if j < num: 
#                 count+=1
#         result_list.append(count)
#     return result_list
    

# nums = [7,7,7]
# print(how_many_smaller(nums))

#*******************************Week5 day1

#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Given the array of integers nums, you will choose two different indices i and j of that array.
# Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
# Example 2:

# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

#expecting int as a return

#class Solution:
# def maxProduct(nums):
#     products = []
#     j = 1
#     for i in range(0, len(nums)-1):
#         #for j in range(1,len(nums)):
#         prod = (nums[i]-1) * (nums[j]-1)
#         products.append(prod)
#         j +=1    
#     return max(products)

# nums = [1,5,4,5]
# print(maxProduct(nums))

#Brians Solution COULD ALSO SORT THE LIST
#  AND then multiply two (largest numbers -1 together)
# def maxProduct(nums):
# 	i_max = 0
# 	for i in range(len(nums)):
# 		if nums[i] > i_max:
# 			i_max = nums[i]
# 			j_max = 0
# 			for j in range(len(nums)):
# 				if i !=j:
# 					if nums[j] > j_max:
# 						j_max = nums[j]
# 	return (i_max -1) * (j_max -1)

# nums = [1,5,4,5]
# print(maxProduct(nums))

#******************week 5 day2
# 1528. Shuffle String
# Add to List
# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.
# List[int]) -> str:
# class Solution:

# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"

# Input: s = "art", indices = [1,0,2]
# Output: "rat"







# def swap( i,j, array):
#     array[i], array[j] = array[j] , array[i]

#Insertion sort to find lowest, to find highest swap the > sign, duh 
# def lowest(numbers):
#     
#         j=i
#         while j > 0 and numbers[j] < numbers[j-1]:
#             #swap(j ,j-1, numbers)
#             numbers[j], numbers[j-1] = numbers[j-1] , numbers[j]
#             j -=1   # this stop the while loop so we can get the next i in the outer loop until we have gone thru the list once
#     return numbers[0]


# def restoreString(str, indices):
#     s_list = list(str) 
#     for i in range(1,len(indices)): # start of and second number because always comparing  the next with the first
#         j = i
#         while j > 0 and indices[j] < indices[j-1]:
#             indices[j], indices[j-1]  = indices[j-1],indices[j]
#             s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
#             j -=1
   
#     return  "".join(s_list)

# indices = [1,0,2]
# print(restoreString("art", indices))


#*****************wb question week5 day3*********************

#   Two Sum

# Solution
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# Test.assert_equals(sorted(two_sum([1234,5678,9012], )), [1,2])
# Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])


# def sumTarget(arr, target):
#     results = []
#     for i in range(len(arr)):
#         for j in range(1,len(arr)):
#             if i != j:
#                 if arr[i] + arr[j] == target:
#                     results.append(arr[i])
#                     results.append(arr[j])
#                     return results         
#     return -1 


# arr = [1234,5678,9012]
# target = 14690
#print(sumTarget(arr, target))


# def two_sum(numbers, target):
#     result = []
#     for i in range(0,len(numbers)):        
#         for j in range(1, len(numbers)):
#             if i != j:
#                 if numbers[i] + numbers[j] == target:
#                     result.append(i)
#                     result.append(j)
#                     return result

#     return result

# {}

# numbers = [2,2,3]
# target = 9
# print(two_sum(numbers, target))

#*******************WB Question week5 day4*************************

#s = "anagram", t = "nagaram"

# s = 'rat'
# t = 'car'

# def anagram(s,t):
#     s_list = sorted(list(s))
#     t_list = sorted(list(t))
#     # better to do 
#     return s_list == t_list

#     # if 
#     #     return True
#     # else:
#     #     return False

# s = "anagram"
# t = "nagaram"

# print(anagram(s,t))

#*********************************weeky day 5

# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
 

# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

# Example 3:
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
 

# Constraints:
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6
   
# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

# def minimumAbsDifference(array):
#     diff_list = []    
#     #if you sort the arrays first, then you would have  the min diff?
#     nums = sorted(array)
#     min_diff = nums[1] - nums[0]
#     for i in range(0, len(nums)-1):
#         if (nums[i + 1] - nums[i]) < min_diff: 
#             min_diff = nums[i +1] - nums[i]
#             diff_list.append([nums[i], nums[i +1]])
#         elif nums[i + 1] - nums[i] == min_diff:             
#             diff_list.append([nums[i], nums[i +1]])
#     return diff_list

# array = [4,2,1,3]
# print(minimumAbsDifference(array))

# Nates
# def minimumAbsDifference(arr):
#     lst = []
#     arr.sort()
#     diff = arr[1] - arr[0]
#     for x in range(1,len(arr)-1):
#         if arr[x+1]-arr[x] < diff:
#             diff = arr[x+1] - arr[x]
#     for x in range(0, len(arr)-1):
#         if arr[x+1]- arr[x] == diff:
#             lst.append([arr[x], arr[x+1]])
#     return lst      

# Asia Bragg  10:11 AM
# arr = [3,8,-10,23,19,-4,-14,27]
# def minimumAbsDifference(arr):
#     arr.sort()
#     new = []
#     min_dif = arr[-1] - arr[0]
#     for num in range(len(arr)-1):
#         if arr[num + 1] - arr[num] < min_dif:
#             new = [[arr[num], arr[num + 1]]]
#             min_dif = arr[num+1] - arr[num]
#         elif arr[num + 1] - arr[num] == min_dif:
#             new.append([arr[num], arr[num + 1]])
#     return new
# print(minimumAbsDifference(arr))

#Brians see wekk 5 screen shots


#************* Week 6 day1 ******************************************
# Electric Company
# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of “F” greater than or equal to 2 returns “Outage”, anything below returns “Power”

#TRY WITH TRUE FALSE

# Example Input: [ T, F, F, F ] 
# Example Output: “Outage”


# #Linear time -   space  close to constant
# def outage(arr):
#     count = 0
#     for char in arr:
#          if char == 'F':
#              count +=1

#     if count >=2:
#          return 'Outage'  
#     else:
#         return "Power" 
# #  Why ar
# arr =  [ 'T', 'F', 'F', 'F' ]  
# print(outage(arr))  


#*******************week 6 day 2**********************

# Check if Number and its double exists
# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 
# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.
# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.
# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

# def ckMultiple(arr):
#     for i in range(0,len(arr)-1):
#         for j in range(1,len(arr)-1):
#             if i != j:
#                 if arr[i] == arr[j] * 2 or arr[j] == arr[i] *2:
#                     return True
#     return False
 
   
# arr = [10,2,5,3]
# arr1 = [7,1,14,11]
# arr2 = [3,1,7,11]
# print(ckMultiple(arr))

#******************week 6 day3  MINE ******************

[0,1,2,2,3,0,4,2]

# WB question

# Remove Element
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length.
# Example 2:
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
# Note that the order of those five elements can be arbitrary.
# It doesn't matter what values are set beyond the returned length.

# I got this right
# time was linear - looping thu the array, space was constant because in place 

# the for loop did not work in this case. got an an index error if I used (len(array-1)) and without it  - it did not catch the last value?

# def removeElement(array, target):
#     while target in array:  
#         array.remove(target)           
#     return len(array)


# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(removeElement(nums,val))

# **************************  Two Sum practice

# Solution
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# Test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])

# def two_sum(number, target):
#      results = []
#      num_list = list(number)
#      for i in range(0,len(num_list)):
#          for j in range(1,len(num_list)):
#              if i != j:
#                  if num_list[i] + num_list[j] == target:
#                     ## this gives sub array if indexes
#                     #results.append([i, j])
#                     results.append(i)
#                     results.append(j)   
#                     return results

# number = [2, 7, 11, 15]
# target  = 9
# print(two_sum(number, target))


#*********************Week7 day1 wb 

# Find Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Example 1:
# Input: [3,0,1]
# Output: 2
# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# def missingNum(nums):
#     nums1 = sorted(nums)
#     missing = 0
#     for i in range(len(nums)-1):
#         if nums1[i] + 1 == nums1[i+1]:
#             continue
#         else:
#             missing = nums1[i+1]-1
#             return missing
         
# arr = [9,6,4,2,3,5,7,0,1]
# print(missingNum(arr))


# *************** CWCharacter with longest consecutive repetition -6
# For a given string s find the character c (or C) with longest consecutive repetition and return:

# # [input, expected],
#     ["aaaabb", ('a', 4)],
#     ["bbbaaabaaaa", ('a', 4)],
#     ["cbdeuuu900", ('u', 3)],
#     ["abbbbb", ('b', 5)],
#     ["aabb", ('a', 2)],
#     ["ba", ('b', 1)],
#     ["", ('', 0)],

# def longest(chars):
#     if chars == "":
#         return '',0
#     max_char = ""
#     max_count = 1
#     count = 1
#     #start at the second value (get around index error?)
#     for i in range(1,len(chars)):
#         #lets you catch the first value
#         if chars[i-1] == chars[1]:
#             count +=1
#             if max_count < count:
#                 max_count = count
#                 max_char= chars[i]
#         else:
#             #reset count
#             count = 1
#     answer = (max_char, max_count)
#     return answer

# chars = "bbbaaabaaaa"
# print(longest(chars))

#******************* WB Week7 day2

# Whiteboard challenge - Find target (Binary Search)
# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

#Should actaully do this as a binary search 

# def findTarget(nums, target):
#     for i in range(1, len(nums)):
#         if nums[i-1] == target:
#             return i-1
        
#     return -1



# nums = [-1,0,3,5,9,12]
# target = -1
# print(findTarget(nums,target))


# def binarySearchHelper(array, target, left, right):
#     while left <= right:
#         middle = (left + right) // 2
#         pot_match = array[middle]
#         if target== pot_match:
#             return middle
#         elif target < pot_match:
#             right = middle -1
#         else:
#             left = middle + 1
#     return -1


# def binarySearch (array, target):
#     return binarySearchHelper(array, target, 0, len(array)-1)

# nums = [-1,0,3,5,9,12]
# target = -1

# print(binarySearch(nums, target))

#  IN JAvascript


# function findTarget(nums,target){
#     for (let i = 1; i< nums.length, i++1){
#         if (nums[i-1)== target{
#             return i-1
#         }
#     }
#     return -1
# }

# function binarySearchHelper(array, target, left, right){

#     while(left <= right){
#         middle = Math.floor(left + right);
#         potential_match = array[middle];
#         if target == potential_match{
#             return middle
#         }else if target < potential_match{
#                 right = middle - 1
#         }else{
#             left = middle + 1
# #         }
# function twoSum(arr,target){
#   for(let i = 0; i < arr.length; i++){
#     for(let j = 1; i < arr.length; j++){
#       if(i + j == target){
#         return [i,j]
#       }
#     }
  # }
  

#     }
#     return -1
# }

# function binarySearch(array, target){
#     return binarySearchHelper( array, target, 0, len(array)-1)
# }



#***********week7 day 3 Two Sum*******************
 #Not Optimal 
# function twoSum(arr,target){
#   for(let i = 0; i < arr.length; i++){
#     for(let j = 1; i < arr.length; j++){
#       if(i + j == target){
#         return [i,j]
#       }
#     }
#   }
  

#Optimal solution ist would user pointers to in one loop OR  using a dictionary
# would be the best solution 

#**************************Week 7 day 4***************************

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# def runningSum(nums):
#   total =0
#   totals = []
#   for num in nums:
#     total+= num
#     totals.append(total)
#   return totals

# nums = [3,1,2,10,1]
# print(runningSum(nums))

# #*****************Algorithm night
# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# def destCity(paths):
#   len_Path = len(paths)
#   dest = paths[len_Path-1][1]
#   return dest

# paths2 =  [["B","C"],["D","B"],["C","A"]]
# paths3 = [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
# print(destCity(paths3))

# destCity(paths):
#   options = []
#   second_check = []
#   for i in range(0,len(paths)):
#     options.append(paths[i][1])
#     second_check.append(paths[i][0])
#     for option in options:
#     if options.count(option) ==1  and second _check.count(option) ==1):
#       return option

# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

# print(destCity(paths))

#**************Wb week8 day1************************

# Given two arrays, write a function to compute their intersection.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.

# def intersection(nums1, nums2):
#     results = []
#     for num1 in nums1:     
#         for num2 in nums2:
#           if num1 == num2 and num1 not in results:         
#             results.append(num1)

#     return results

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(intersection(nums1, nums2))

#goggled answer
#https://www.geeksforgeeks.org/python-intersection-two-lists/

# def intersection(nums1, nums2):
#   return list(set(nums1) & set(nums2))


# nums1 = [4,9,5,11,9,5,8]
# nums2 = [9,4,9,8,4]
# # nums1 = [1,2,2,1]
# # nums2 = [2,2]
# print(intersection(nums1, nums2))


#Joel's answer

# def intersection(nums1, nums2):
#     temp = set(nums1)
#     if len(nums2) > len(nums1):
#       temp = set(nums2)
#       newList = [value for value in nums1 if value in temp]
#     else:
#       newList = [value for value in nums2 if value in temp]\
#     return list(set(newList))


#**************Wb week8 day2************************

# Return the number of negative numbers in grid.
 
# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
# Input: grid = [[-1]]
# Output: 1

# def remove_neg(a_list):
#   count = 0
#   for sublist in a_list:
#     for element in sublist:
#       #print(element)
#       if element < 0:
#         count +=1
#   return count

# a_list = [[3,2],[1,0]]

# print(remove_neg(a_list))

#Mikes solution - Botha are slow
# def countNeg(x):
#     count = 0
#     for i in range(0,len(x)):
#         for j in x[i]:
#             if j < 0:
#                 count += 1
#     return count
# print(countNeg([[1,-1],[-1,-1]]))       

# occurrences = collections.Counter(a_list)

# object resembles a dictionary

# print(occurrences)
# OUTPUT
# Counter({'a': 2, 'b': 1})
# print(occurrences["a"])





#**********************Wb week8 day 3**************************

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
 
# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
#take back half and put it in the frounf half

# import math

# def shuffle(nums, n):
#   j = (len(nums)/2)

#   for i in range(1,len(nums)):
#     nums[i], nums[j] == nums[j], nums[i]
#   return nums

# nums = [2,5,1,3,4,7]
# n = 3 
# print(shuffle(nums,n))

# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Example 1
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
# Example 2:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.
# Example 3:
# Input: s = "aiohn", indices = [3,1,4,2,0]
# Output: "nihao"
# Example 4:
# Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
# Output: "arigatou"
# Example 5:
# Input: s = "art", indices = [1,0,2]
# Output: "rat
# Collapse

# def restoreString(str, indices):
#     s_list = list(str) 
#     for i in range(1,len(indices)):
#         j = i
#         while j > 0 and indices[j] < indices[j-1]:
#             indices[j], indices[j-1]  = indices[j-1],indices[j]
#             s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
#             j -=1
   
#     return  " ".join(s_list)

# indices = [4,0,2,6,7,3,1,5]
# print(restoreString("aaiougrt", indices))

# Brians Practice interview question with me - Spet 8, 2020
# Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.


# Example 1:

# Input: aa
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
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

# def uniqueOccurrences(arr):
#   arr_dict={}
#   for i in range(0, len(arr)):
#     if arr[i] not in arr_dict:
#       arr_dict[arr[i]] = 1
#     else:
#       arr_dict[arr[i]] +=1

#   results = []
#   for value in arr_dict.values():
#     if value not in results:
#       results.append(value)
#     else:
#       return False
#   return True    

# arr = [1,2]
# print(uniqueOccurrences(arr))



# Given an integer n, return any array containing n unique integers such that they add up to 0.
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# class Solution(object):
#     def sumZero(self, n):
#         """
#         :type n: int
#         :rtype: List[int]
# #         """
# b = [1,2,3]
# print(b)
# b.sort(reverse = True)
# print('Hello',b)


# ****************************CodeSigna/ questions 

# def countTinyPairs(a, b, k):
#   count = 0
#   #b = b[::-1]
#   for i in range(0,len(a)):      
#           #print(j)
#           stri = str(a[i])
#           j = b[(len(b)-1)-i]
#           strj = str(j)
#           num_str = stri + strj
#           if int(num_str) < k:
#               count+=1
#   return count

# a = [1,2,3]
# b = [1,2,3]
# k = 32
# print(countTinyPairs(a,b,k))


a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]

# answer 
# meanGroups(a) = [[0, 4],
#                  [1],
#                  [2, 3]]

# def meanGroups(a):
#      means = []
#     for i in a:
#         mean = sum(a[i])/len(a[i])
#         if mean not in means:
#             means.append[[mean]]
#         else:


# Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

# Example

# For a = [10, 2], the output should be concatenationsSum(a) = 1344.

# a[0] ∘ a[0] = 10 ∘ 10 = 1010,
# a[0] ∘ a[1] = 10 ∘ 2 = 102,
# a[1] ∘ a[0] = 2 ∘ 10 = 210,
# a[1] ∘ a[1] = 2 ∘ 2 = 22.
# So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

# For a = [8], the output should be concatenationsSum(a) = 88.

# There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.
# def concatSum(a):
#     total = 0
#     total_list = []
#     str_a = str(a)
#     for i in range(0, len(a)):
#         for j in range(0,len(a)):
#           str1 = str(a[i]) + str(a[j])
#           total_list.append(int(str1))
#     return sum(total_list)      

# a = [8]

# print(concatSum(a))



# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.

# 7 and 3 produce the largest product.


# def adjacentElementsProduct(inputArray):    
#     max_prod = 1
#     max_prod = inputArray[0] * inputArray[1]
#     for i in range(1,len(inputArray)):            
#         if inputArray[i-1] * inputArray[i] > max_prod:
#              max_prod = inputArray[i-1] * inputArray[i] 
#     return max_prod



# inputArray = [5, 1, 2, 3, 1, 4]     #= 6
# inputArray1 =  [5, 6, -4, 2, 3, 2, -23]     #= 30

# print(adjacentElementsProduct(inputArray))

# Easy

# Codewriting

# # 300

# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

# Example

# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.

# Ratiorg needs statues of sizes 4, 5 and 7.

# def makeArrayConsecutive2(statues):
#     statues1 = sorted(statues)
#     count = 0
#     for i in range(0,len(statues1)-1):
#         if statues1[i+1] != statues1[i] + 1:
#             count+=1
#     return count

# statues = [6, 2, 3, 8]
# print(makeArrayConsecutive2(statues))

# 
# John works at a clothing store. He has a large pile of socks that he must
#  pair by color for sale. Given an array of integers representing the
#   color of each sock, determine how many pairs of socks with matching colors there are.

# For example, there are  socks with colors .
#  There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

# Function Description

# Complete the sockMerchant function in the editor below.
#  It must return an integer representing the number of matching pairs of socks that are available.

# sockMerchant has the following parameter(s):

# n: the number of socks in the pile
# ar: the colors of each sock


def sockMerchant(n,arr):
    pairs = 0
    sock_dict = {}
    for i in range(0,len(arr)):
        if arr[i] not in sock_dict:
          sock_dict[arr[i]] = 1
        else:
          sock_dict[arr[i]] +=1

    for value in sock_dict.values():
       if value//2 > 0:
         pairs += value//2
    return pairs
n = 9      
arr = [10 ,20, 20 ,10,10, 30, 50 ,10 ,20 ]
print(sockMerchant(n,arr))     


https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup






# # For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# # adjacentElementsProduct(inputArray) = 21.

# # 7 and 3 produce the largest product.


# def adjacentElementsProduct(inputArray):    
#     max_prod = 1
#     for i in range(1,len(inputArray)): 
#         max_prod =   inputArray[i-1] * inputArray[i]    
#         if inputArray[i-1] * inputArray[i] >= max_prod:
#              max_prod = inputArray[i-1] * inputArray[i] 
#     return max_prod

# print(adjacentElementsProduct(inputArray))

# inputArray = [5, 1, 2, 3, 1, 4]     #= 6
# inputArray1 =  [5, 6, -4, 2, 3, 2, -23]    #= 30
