
#****CHECK SPELLING, PRINT BRACKETS,COLONS

## Week2 day2*Given a number as an input, print "Fizz" if the number is even,
#  "Buzz" if the number is odd.#


#Questions? -  only integers, are they all > 0

def fizz_buzz(num):
    if num % 2 == 0:
        print("Fizz")
    else:
        print("Buzz")


num = 4
num1 = 7
fizz_buzz(num1)


#  List comp for fizz buzz range problem
  obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

# Week2 day3Given a string as a parameter to a function,
#  return True if the string is a palindrome and False if not

#Question - can we have capital letters ?
#          - can I assume there are no special characters or number in the string?

#slicing is start, stop(exclusive), step 

def palindrome(str1):
    if str1.lower() == str1.lower()[::-1]:
        print("Yes, this is a palindrome")
    else:
        print("Not a palindrome")

str1 = 'Racecar'
str2 = 'asdhf'
palindrome(str2)

#Best time and space
O(n) time Go through string once but O(1) Constatn spave , only
using the pointers, nothing depends on size of the string for space complexity

def isPalindrome(string):
    #start of string
    left_idx = 0
    #end of string
    right_idx =  len(string) - 1
    while left_idx < right_idx:
        # if you start at the begining of the word and the end of the word,
        # the leters will be the same as you work your way to the middle if it is a palindrome
        if string[left_idx] != string[right_idx]:
            return False
        left_idx +=1
        right_idx -= 1
    return True




#Week2 day4*******#Find all the even numbers for a list and put them in a new list
#Questions - the lists just have numbers, and all integers, and no zero
 

def even_odd(numbers):
    #even_list = []
    even_list = [num for num in numbers if num % 2 == 0 ]
    # for num in numbers:
    #     if num % 2 == 0:
    #         even_list.append(num)
        
    return even_list
        
a_list = [2, 7, 9, 4, 8, 7]
print(even_odd(a_list))

#**********Week3 Day1 # Remove Element
# Given a list of numbers and a value as input to a function, remove all instances of that value "in-place" and return the new length of the list
# Input: nums = [3,2,2,3] value = 3
# Output: return a length == 2

def remove_element(nums,target):
    while target in nums:
        nums.remove(target)
    return len(nums)

or

def remove_element(nums,target):
    for num in nums:
        if target == num:
            nums.remove(target)
    return len(nums)

target = 3
nums = [3,2,2,35,3,7,-3]
print(remove_element(nums, target))


# #******************week3 day2 - Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “),
# return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.

# Example Input: “Hello World”
# Example Output: 5
# Example Input 2: “The brown loud cow plowed”
# Example Output 2: 6


def find_length(str1):
    def word_length(str1):
    word_list = str1.split(" ")
    # last_word = word_list[-1] # this turns the string into a list, and the last word in the list is [-1]
    # length= len(last_word)
    return len(word_list[-1])


str1 =  "Hello World"
str2 = "The brown loud cow plowed"
print(word_length(str2))

#*******************week3 day3 remove vowels
# Create a function that given a string remove the vowels in the string and return the string.
# Example Input: “Joel”
# Example Output: “Jl”

def removeVowels(str1):
    vowels = "aeiou"
    for char in str1:     
        if char in vowels:
            str1 = str1.replace(char, "")       
           
    return str1

str1 = "Joel Carter  Ebanezer Scrooge, Cindy  Lee Stevenson"
print(removeVowels(str1))

#Better solution ONE LINE   with regex
 # Python program to remove vowels from a string 
# Function to remove vowels 
  
# import the module for regular expression (re) 
import re 
def rem_vowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))             
  
# Driver program 
string = "GeeksforGeeks - A Computer Science Portal for Geeks"
print rem_vowel(string)  


#*********************Binary Search Practice Week 3
# Time complexity - O(log n) logrithmic we for not have to traverse the whole array, we are splitting the array if half for the seach every time we go through the while loop - better than the linear

# Space complexity - O(1) - constant, just meed to keep track couple of variables - the space does not depend on the length of the array 
#                                                               
# arguments are: list of nums, the num we are trying to find, the start (aka index0) of the array, 
#                 and the end of the array (aka last index (len(array)-1)
#Std practice is to define a helper function


# input - sorted integer array and target integer
# output - return the index of the target, or -1 if not found
# edgcases -
# assumptions - the array will not be empty?


def binarySearchHelper(array, target, left, right):
    # are we at the end of the array?
    while left <= right:
        #talking middle index here
        middle = (left + right) // 2 # floor division to account for an uneven number of numbers in the array
        # first guess, maybe we will get lucky and the target will be found right at the middle index,
        # if not keep moving dividing the narrowed down search area for the target         
        potentialMatch = array[middle]
        if target == potentialMatch:
            return f"The index of the target is {middle}"
        elif target < potentialMatch:
            right = middle - 1    # move to the left side of middle(dividing by 1/2 again)
        else:
            left = middle + 1     # move to the right side of middle(dividing by 1/2 again)

    return -1  # this means target was not found

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

print(binarySearch([1,5,111,23], 23))


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
#***********************
'''
Converting a list to dictionary with list elements as keys in dictionary
All keys will have same value BUT KEYS AHVE TO BE UNIQUE
''' 
dictOfWords = { i : 5 for i in listOfStr } thsi is for keys and they have to be unique

Here the values are the list elements ad the keys are the indexes
dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr) ) }
#*****************************************

def find_smallest(numbers):     
     numbers.sort()
     return numbers[0]


#f you can't use sort mothod, you could change the list into a dict for better runtime, butyou would use more space. It would depend on the length of you list
#  but here you need more space #because you create a dictionary

numbers = [50,30,4,2,11,0]
numbers2 = [40,3,4,2]

print(find_smallest(numbers))



#***********good dictionary/string/list problem from week3-day3 Exercise 2
### Exercise #2 <br>
#Create a function that counts how many distinct words are in the string below.
#Then outputs a dictionary with the words as the key and the value as the amount of times
#that word appears in the string.<br>
import re



def distinctWords(a_text):
    #take out all punctation from string
    str1 = re.sub(r'[,.:@#?!&$]', '', a_text)  
    word_dict = {}
    word_list = str1.lower().split()   # coould have done this  here --  sorted(word_list = str1.lower().split())          
    word_list.sort()
   
    for word in (word_list):
        if word.lower() not in word_dict:
            word_dict[word.lower()] = 1   # the 1 is the frequency (count) of the word in the string
        else:        
            word_dict[word.lower()]+=1     # now there is another one frequency (count) of the word in the string               

    for key, value in word_dict.items():
         print(key, ' : ', value) 
            
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

distinctWords(a_text)

#****************** my question1 **************
# # print out the index of each letter of a string
for (i, item) in enumerate('hey', start=1):
    print(i, item)

def printStrIndex(str1):    
    for index, key in enumerate(str1, start =0):
        print(index,key)

str1 = " Cindy Lee"
printStrIndex(str1)


 #*************   my Question2**************
 # print out the value and each index of a list 
# using naive method to 
# get index and value 

def printList(aList):
    for i in range(len(aList)):
        print(f" for index{i} the letter is {aList[i]}")

aList = ['c','i','n','d','y']
printList(aList)
	
#********************myQuestion3******************

# For a given number num, write a function to test if it's a numerical palindrome or not and
#  return a boolean (true if it is and false if not).
# Return "Not valid" if the input is not an integer or less than 0.

def numPalindrome(num):
    # if the string equals the string in reverse  then true
    if type(num) == int and num > 0:
        num_str = str(num)
        if num_str == num_str[::-1]:
            return True
        else:
            return False
    else:
        return "Not Valid"
#Codewars solution
# def palindrome(num):
#     if type(num) == int and num > 0:
#         return str(num) == str(num)[::-1]
#     else:
#         return 'Not valid'


num = 5432,2341
print(numPalindrome(num))

#************************** recursive factorial function Week3-day2***************
# this is 5! = 5 * 4 * 3 * 2 * 1

#This starts at 5, then goes down the stack  until 1(or2?) then starts multiplying the values to itself up the stack
#  1 *1 = 1  1*2 = 2  2*3 = 6  6*4 = 24 24*5 = 120   5 is the number we passed to the function
#  
def factorial(n):
    if n <= 1:
        return 1   #no factorial for zero and the factorial of 1 is 1
    else:
        return n * factorial(n-1)
print(factorial(5))


def factorial(n):
    answer = 1
    i = 1
    while i <= n:
      answer = answer * i     
      i+=1

    return answer

        
print(factorial(5))


def factorial(n):
  answer = 1
  for i in range(1, n+1):
    answer *= i
  return answer

n =5
print(factorial(n))





#******************* Recursive fibonnaci function*****************************
# f{n}=F{n-1}+F{n-2} for n > 2
# using 5 
#iteration0 =1   
# iteration0 =1
# iteration0 =2    n       n
# iteration0 = 3  (3-1) + (3-2) = 3
# iteration0 = 5  (4-1) + (4-2) =  5 
# iteration0 = 8  (5-1)  + (5-2) = ????
# 
def fibonacci(num):
    if num <= 2:
        return num
    else:       
        return fibonacci(num-1) + fibonacci(num-2)
    
print(f"Last interation result is {fibonacci(5)}")


#*******************MINE WITH FOR LOOP
# The fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, ...
def fib(n):
    #initialize the list with starting elements: 0, 1
    fibonacciSeries = [0,1]
    if n > 2:
      for i in range(2,n):
        next_element = fibonacciSeries[i-1] + fibonacciSeries[i-2]
        fibonacciSeries.append(next_element)
    return fibonacciSeries

n = 5
print(fib(n))


#***************** In-Place or swap Week3day3 ****************
def swap(a_list, x ,y ,z):
    a_list[x], a_list[y], a_list[z] =  a_list[z], a_list[y], a_list[x]

my_list = [10, 20, 70, 125,55, 94]
print(my_list)

swap(my_list,3,4,5)
print(my_list)


#***************** Two Pointers Week3day3 ****************
#This reverses the list
def twoPointers(alist):
    left = 0
    right = len(alist) -1

    while left <= right:
        alist[left], alist[right] = alist[right], alist[left]
        left = left + 1
        right = right - 1
    return alist
    
alist = [8,7,6,55,66,77]
print(twoPointers(alist))


#***************** Bubble Sort Week3day3 ****************

Bubble Sort
# Worst Case: O(n^2) Time - O(1) Space
#Best case time would be linear O(n) if the array is sorted- still have to go through the array  once to check. 
# //O(n^2) time depending on n the length of the array quadratiec -  looping through the array MULTIPLE times (not just once)  until the array is sorted
# //O(1) space is constant doing swap in place - didn't allocate additional memmory

#Helper function first
def swap(i,j,array):
    array[i], array[j] = array[j], array[i] # these are index numbers
    
    
def bubbleSort(array):
    #Flag or pointer to confim sort
    isSorted = False
    while not isSorted:  #This means while Is sorted is True , but we cant; use it here# we need to go through this loop at least once to se if the list is sorted      
        isSorted = True   # we need this to catch when the array has been sorted. See comments below
        for num in range(len(array)-1):   #num is index and len(array)-1 is the last index number
            if array[num] > array[num+1]:
                swap(num, num+1, array)
                isSorted = False
    return array

bubbleSort([20,20,50,7,6,5,10])


#Once the array has sorted once gone through the for loop the isSorted value is false,


#***************WB Week3 Day1 -Non repeating characters

# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1.
# Examples:
# Input - s = "leetcode"
# Output - return 0
# Input - s = "loveleetcode"
# Output - return 2
#  'aaa' return  -1


def firstUniqChar(s):
    letter_dict = {}
    # for each letter in the string if it is not in the dictionary add it
    # and the count will be one. The key for the dict is the string letter
    #and the values is the frequency of the letter
    for char in s:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            # if it is in the dictionay add one to the exiting letter coint
            letter_dict[char] += 1
    #loop throught the dictionary annd find the first non repeating letter(the count or value)will be one      
    for char in s:
        #want the  Key of the first letter in the string that has a count of 1
        # return that index of the string for that letter
        if letter_dict[char] == 1:
            return s.index(char) # the return is like a break, it stops the for loop
                                  #one this is found we are done
    # here the forloop has gone through all the letters in the string and no letter had a frequency of one
    #  so there are no unique letters
    return -1

print(firstUniqChar('lllll'))


#******************WB Question Week4 day2


# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false  
# 

#check ing for alpha numeric charcters
# .isalnum
# .isalpha
# .isnumeric

import re
def palindrome(str1):
    str2 = re.sub(r'[,.:@#?!&$]', '',str1)
    str2 = str2.replace(" ", "")
    str2 = str2.lower()
    if str2 == str2[::-1]:
        return True
    else:
         return False
    
str1 = "race a car"
str2 = "A man, a plan, a canal: Panama"
print(palindrome(str1))

#Brians  one liner

# def isPal(s):
#     s_as_lst = [x.lower() for x in s if x.isalnum()]
#     return s_as_lst == s_as_lst[::-1]
        
# str1 = "race a car"
# str2 = "A man, a plan, a canal: Panama"

# print(isPal(str2))

def isPal(s):
    s = s.lower()
    a_list = []
    for char in s:
        if char.isalnum():
            a_list.append(char)
    if a_list ==a_list[::-1]
        return True
    else:
        return False

str1 = "race a car"
str2 = "A man, a plan, a canal: Panama"
print(isPal(str2))

# Example 1:
# Input: aa
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

def uniqueOccurrences(arr):
  arr_dict={}
  for i in range(0, len(arr)):
    if arr[i] not in arr_dict:
      arr_dict[arr[i]] = 1
    else:
      arr_dict[arr[i]] +=1

  results = []
  for value in arr_dict.values():
    if value not in results:
      results.append(value)
    else:
      return False
  return True    

arr = [1,2]
print(uniqueOccurrences(arr))

#***********************************week4 day3 WB

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

def reverseDigit(n):
    neg = "n"
    if n < 0:
        neg = 'y'
        n = n * -1
    num_str = str(n)

    #DONT NEED THIS PYTHON DROPS THE the zero when it turns the string back into a zero
    # for n in num_str:
    #     if n == 0 :
    #         num_str.replace(n, "")

#     num_str2 = num_str[::-1]
#     num = int(num_str2)
#     print(num)

#     if neg == 'y':
#         num = num * -1
#     return num

# print(reverseDigit(130))



#********************************week4 day5 I got this one

# thsi is what  Brian had to create the linked list
#initializing an empty linked list
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
#     def __str__(self):
#         return str(self.val)

# #Create and Connect the nodes with the class above
# five = ListNode(5)
# four = ListNode(4, five)
# three = ListNode(3, four)
# two = ListNode(2, three)
# one = ListNode(1, two)

# def reverseList(head):
#     current = head
#     following = head
#     previous = None
#     while current is not None:
#         following  = following.next
#         current.next = previous
#         previous = current
#         current = following
#     return previous.val    

# print(reverseList(one))

#******Brians way
# def reverseList(head): # starts at the head which is one
#     current = head # this in value = 1, .next(pointer is pointing to 2)
#     prevoius = None  # there is not a previous value or pointer yet, but need to initialize it

#     while current:  # once the loop get to 5, there is no pointer vales ans this loop fails
#         # temp is place holder, so we know that we started at l , with  next pointing to 2   
#         temp = current
#         #the line below makes current.next is pointing to the next popinter which is two 
#         # temp is still pointing to pointer1   
#         current = current.next
#         temp.next = prevoius
#         prevoius = temp
#     return temp   
    
#print(reverseList(one))



#***************************Week4 day5**************************
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

def how_many_smaller(nums):    
    result_list = []
    for num in nums: # both loops use the same list/array
        count = 0
        for j in nums:
            if j < num: 
                count+=1
        result_list.append(count)
    return result_list
    
 nums = [7,7,7]
print(how_many_smaller(nums))
    


#**********Randon number generator
from random import randint
#used to genetate list of 5 numbers from 0 - 20

nums = [randint(0,20) for i in range(5)]

#****************week5 day2*******************
def restoreString(str, indices):
    s_list = list(str) 
    for i in range(1,len(indices)):
        j = i
        while j > 0 and indices[j] < indices[j-1]:
            indices[j], indices[j-1]  = indices[j-1],indices[j]
            s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
            j -=1
   
    return  " ".join(s_list)

indices = [4,0,2,6,7,3,1,5]
print(restoreString("aaiougrt", indices))

#*******************codewars quesition

##cleaning up file names

#  1231231223123131_myFile.tar.gz2

#  1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34

def extract_file_name(dirty_file_name):
    a = dirty_file_name.find('_')
    b = dirty_file_name.rfind('.')
    c = dirty_file_name[a+1:b]
    return c


s='1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION'

print(extract_file_name(s))


#************codewars Question 

# MexicanWave
# Rules
# 1.  The input string will always be lower case but maybe empty.
# 2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
# wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# result = [" Gap ", " gAp ", " gaP "]
#  ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]

def wave(word):
    result = []
    letters= []
    letters = list(word)
    for i in range(len(word)):
        if letters[i] == " ":
                pass
        else:
            letters[i] = letters[i].upper()
            up_word = "".join(letters)
            result.append(up_word)
            letters[i] = letters[i].lower()
    
    return result

word = 'two words'
print(wave(word))

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
# Test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# Test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])


def two_sum(numbers, target):
    result = []
    for i in range(0,len(numbers)):        
        for j in range(1, len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

    return result



numbers = [2,2,3]
target = 9
print(two_sum(numbers, target))

#*******************WB Question week5 day4*************************

#s = "anagram", t = "nagaram"

# s = 'rat'
# t = 'car'

def anagram(s,t):
    s_list = sorted(list(s))
    t_list = sorted(list(t))
    # better to do 
    return s_list == t_list

    # if 
    #     return True
    # else:
    #     return False

s = "anagram"
t = "nagaram"

print(anagram(s,t))

#*********************************week5 day 5
# appending nested lists, appending sublists
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

def minimumAbsDifference(array):
    diff_list = []    
    #if you sort the arrays first, so you have the
    # sequential order of the digits 
    nums = sorted(array)
    #this subtracts the last number(highest)
    #from the first number(lowest) so we know
    #all diff have to be smaller than this
    # we don't worry about absolutes , we are always 
    #subtracting the next num from prev num
    min_diff = nums[-1] - nums[0]
    for i in range(0, len(nums)-1):
        if (nums[i + 1] - nums[i]) < min_diff: 
            min_diff = nums[i +1] - nums[i]
            diff_list.append([nums[i], nums[i +1]])
        elif nums[i + 1] - nums[i] == min_diff:             
            diff_list.append([nums[i], nums[i +1]])
    return diff_list

array = [1,3,6,10,14, 15]
print(minimumAbsDifference(array))

#Brians see wekk 5 screen shots


##*************mine GET MAX VALUE WITH THE KEY DICTIOARY
return (max(s_dict.items(),key = lambda i: i[1]))


##**********Get alphabet ranking dictionary:
letter_scores = dict(zip(string.ascii_lowercase, range(1, 27)))

#****************find all occurences of a substring

import re 
def get_order(order): 
    new_order = []
    foods = ['burger', 'fries', 'chicken', 'pizza','sandwich','onionrings', 'milkshake', 'coke']
    for food in foods:
        for m in re.finditer(food, order):
            #print(food, m.start(), m.end())
            new_order.append(food)

    new_str = (' '.join(new_order)).title()
    return new_str

order = "pizzachickenfriesburgercokemilkshakefriessandwich"
print(get_order(order))


# Born a misinterpretation of this kata, your task here is pretty simple: given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.
# For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], as the first one takes [1,3,5], the second collects [2,4].
# The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3], as they will respectively take [1,4], [2,5] and [3].

# Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will of course take nothing (0).
# Note: in case you don't get why this kata is about English beggars, then you are not familiar on how religiously queues are taken in the kingdom ;)

# Test.describe("Basic tests")
# Test.assert_equals(beggars([1,2,3,4,5],1),[15])
# Test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
# Test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
# Test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
# Test.assert_equals(beggars([1,2,3,4,5],0),[])

def beggars(values, n): 
    beggar_count = n
    results = []
    total = 0
    start=-1
    while n > 0:
        start +=1
        total = 0
        for i in range(start, len(values), beggar_count):
            total  += values[i]
        results.append(total)            
        n -=1       
    return results

values = [1,2,3,4,5]
n = 0
print(beggars(values,n))


##*****************sorting a dictioary by values descending

    #we have created a lambda function and passed the values of the dict as argument to it by iterating #through the dict by values i.e. item[1].
    sort_dict= dict(sorted(a_dict.items(), key=lambda item: item[1], reverse= True)) 



#**************** Simple frequency sort_6

# I DIDN"T THINK TO SORT THE ARRAY FIRST....duh had everythinf else.
# In this Kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# --we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
def solve(arr):
    a_dict = {}
    for item in sorted(arr):
        if item not in a_dict:
            a_dict[item] = arr.count(item)
    high_freq = sorted(a_dict, key = a_dict.get, reverse = True)
    result = []
    for i in high_freq:
        result += ([i] * a_dict[i])
    return result

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

# the for loop did not work in this case. got an an index error if I used (len(array-1)) and without it  - it did not catch the lasy value?

def removeElement(array, target):
    while target in array:  
        array.remove(target)           
    return len(array)


nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))


#**********Insertion Sort
#Helper function first
def swap(i,j,array):
    array[i], array[j] = array[j], array[i] 
    


    
def insertionSort(array):
    for i in range(1,len(array)):  #Not -1   start at index1 (lookin at the vaue first NEXT to the first number and using the lenght of the array no the incex numbeer
       #in the arraythis time going past the array
        j = i  #poiunter as a placeholder not we can increemtn i 
        while j > 0 and array[j] < array[j-1]:   #looking backward
            swap(j, j-1, array)
            j-=1
    return array

print(insertionSort([10,50,30,2,1]))


#All in one 
def insertionSort(array):
    for i in range(1,len(array)):  #Not -1   start at index1 (lookin at the vaue first NEXT to the first number and using the lenght of the array no the incex numbeer
       #in the arraythis time going past the array
        j = i  #poiunter as a placeholder not we can increemtn i 
        while j > 0 and array[j] < array[j-1]:   #looking backward
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
    return array

print(insertionSort([10,50,30,2,1]))


##***************good string manipulation or list

# Backspaces in string
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.

# Test.assert_equals(clean_string('abc#d##c'), "ac")
# Test.assert_equals(clean_string('abc####d##c#'), "" )
# Test.assert_equals(clean_string("#######"), "" )
# Test.assert_equals(clean_string(""), "" )


def clean_string(s):
    result = []
    for c in s:
        if c == '#':
            if result:
                result.pop()
        else:
            result.append(c)
    return ''.join(result)


def clean_string(s):    
    ans=""
    for letter in s:
        if letter == "#":
           if len(ans)> 0:
              ans = ans[:-1]
        else:
           ans += letter

    return ans

 #**********************PRACTICE *************************

#Keeping track of two totals

 
 # Character with longest consecutive repetition -6
# For a given string s find the character c (or C) with longest consecutive repetition and return:

# # [input, expected],
#     ["aaaabb", ('a', 4)],
#     ["bbbaaabaaaa", ('a', 4)],
#     ["cbdeuuu900", ('u', 3)],
#     ["abbbbb", ('b', 5)],
#     ["aabb", ('a', 2)],
#     ["ba", ('b', 1)],
#     ["", ('', 0)],



def longest_repetition(chars):    
    if len(chars) == 0:
        return '', 0        
    max_char = chars[0]
    max_count = 1    
    count = 1
    for i in range(1,len(chars)):        
        if chars[i-1] == chars[i]: #bypasses index error?
            count += 1        
            if max_count < count:
                max_char = chars[i]
                max_count = count
        else:
            count = 1
    
    return max_char, max_count
chars = "aacccbddddddaaaa"
print(longest_repetition(chars))    




#*********************Week7 day1 wb 

# Find Missing Number
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Example 1:
# Input: [3,0,1]
# Output: 2
# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

def missingNum(nums):
    nums1 = sorted(nums)
    missing = 0
    for i in range(len(nums)-1):
        if nums1[i] + 1 == nums1[i+1]:
            continue
        else:
            missing = nums1[i+1]-1
            return missing
         
arr = [9,6,4,2,3,5,7,0,1]
print(missingNum(arr))


##***********************Sorting string alpabetically regardless of case 
 new_str = sorted(s, key=lambda new_str: (new_str.lower(), new_str.islower()))

 ##**********************Math.floor
 The math. floor() method rounds a number downwards to the nearest integer, and returns the result.
 math.floor(1.4) => 1
 math.floor(5.3) => 5
 math.floor(-5.3) => -6  BECAUSE ROUNDS DOWNWARD
 math.floor(22.6) =>22



#TWO pointer comparison
#  // Naive solution to find if there is a 
# // pair in A[0..N-1] with given sum. 
  
bool isPairSum(A[], N, X) 
{ 
    for (i = 0; i < N; i++) { 
        for (j = 0; j < N; j++) { 
            if (A[i] + A[j] == X) 
                return true; // pair exists 
  
            if (A[i] + A[j] > X) 
                break; // as the array is sorted 
        } 
    } 
  
    // No pair found with given sum. 
    return false; 
} 
# The time complexity of this solution is O(n2).

// Two pointer technique based solution to find 
// if there is a pair in A[0..N-1] with a given sum. 
bool isPairSum(A[], N, X) 
{ 
    // represents first pointer 
    int i = 0; 
  
   # represents second pointer 
    int j = N - 1; 
  
    while (i < j) { 
  
        # If we find a pair 
        if (A[i] + A[j] == X) 
            return true; 
  
        // If sum of elements at current 
        // pointers is less, we move towards 
        // higher values by doing i++ 
        else if (A[i] + A[j] < X) 
            i++; 
  
        // If sum of elements at current 
        // pointers is more, we move towards 
        // lower values by doing j-- 
        else
            j--; 
    } 
    return false; 
} 

# The above solution works in O(n)

# How does this work?
# The algorithm basically uses the fact that the input array is sorted. We start the sum of extreme values (smallest and largest) and conditionally move both pointers. We move left pointer i when the sum of A[i] and A[j] is less than X. We do not miss any pair because the sum is already smaller than X. Same logic applies for right pointer j.

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

#1304.LeetCode-  Find N Unique Integers Sum up to Zero Sept # #         """10,2020

# Given an integer n, return any array containing n unique integers such that they add up to 0.
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# class Solution(object):
#     def sumZero(self, n):
#         """
#         :type n: int
# #         :rtype: List[int]


# *************codewars6**************String array duplicates
# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

# For example:
# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].
# dup(["kelless","keenness"]) = ["keles","kenes"].

# Strings will be lowercase only, no spaces. See test cases for more examples.
# Test.it("Basic tests")
# Test.assert_equals(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]),['codewars','picaniny','hubububo'])
# Test.assert_equals(dup(["abracadabra","allottee","assessee"]),['abracadabra','alote','asese'])
# Test.assert_equals(dup(["kelless","keenness"]), ['keles','kenes'])
# Test.assert_equals(dup(["Woolloomooloo","flooddoorroommoonlighters","chuchchi"]), ['Wolomolo','flodoromonlighters','chuchchi'])
# Test.assert_equals(dup(["adanac","soonness","toolless","ppellee"]), ['adanac','sones','toles','pele'])
# Test.assert_equals(dup(["callalloo","feelless","heelless"]), ['calalo','feles','heles'])
# Test.assert_equals(dup(["putteellinen","keenness"]), ['putelinen','kenes'])
# Test.assert_equals(dup(["kelless","voorraaddoosspullen","achcha"]), ['keles','voradospulen','achcha'])
# Good luck!
# If you like this Kata, please try:

#for i in range(1,n+1):
def sumZero(n):
    num_list = []
    for i in range(n//2):      
        if n not in num_list:
            num_list.append(i +1)
            num_list.append(-(i+1))  
    if n%2 != 0:
        num_list.append(0)
    return num_list
            

print(sumZero(5))

##Python solution for  AE Valid Subsequence Easy

#O(n)- linear time loop through the array once - n is the length of the main array
#O(1) - constant  space because we are just storing the two index variable, nothing that increases with the size of the inputs

def  isValidSubsequence(array, sequence):
    #  traverseing through both arrays at the same time with pointers keeping track of  the indexes
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            #we have found a match so look for the next value in 
            #the sequence, we only move the seq index when we find a match
            seqIdx += 1
        #now check the next value in the main array
        arrIdx += 1
    #if we have gone through the entire sequesnce we know we have a valid
    #subsequnce because we only moved it fowrard when we had a match
    # if seqIdx == len(sequence):
    #     return True
    # else:
    #     return False
    # or  
    return seqIdx == len(sequence)  
  

array =  [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))


#Binary Search Tree aka BST 
def findClosestValueInBst(tree, target):
                                #here initializing closest value as infinity, could use the root node if you wanted
    return findClosestValueInBstHelper(tree,target, float("inf"))

def findClosestValueInBstHelper(tree,target, closest):
    #need a variable that points(keeps track) of the current node
    currentNode = tree
    #while we are not dealing with a leaf or bottom of the tree    
    while currentNode is not None:    
        #otherwise we want the ABS difference between the
        #closest node and the target node
        #if the abs(target - closest) is > abs(target - tree.value)
        #then update closest
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
            #here we decide which side of the tree we need to go down
            # if target is less than the tree.value(root node) then go down the left side
        if target < currentNode.value:
            currentNode = currentNode.left
        # if target is greater than the currentNode.value(root node) then go down the right side
        elif: target > currentNode.value:
            ccurrentNode = currentNode.right
        else:
            break
    return closest

#*******************************   
#Product Sum
# time complexity  - quadratic O(n^2) = with n the length of the array
# space compexity - constant O(n) - only 1 extra variable 

def productSum(array, depth = 1):
    total_sum = 0   
    for element in array:        
        if type(element) is list:  
            total_sum += productSum(element, depth +1)               
        else:
             total_sum += element
    return total_sum * depth

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))

#answer = 5 +2 +(2 * (7 + -1 ) + 3 + (2 * ( 6 + (3 *(-13 + 8)  + 4)

#BST Node Depths
the distance betweena node ina BT and the tree's root is called the nodes's depth

class BinaryTree:
    def __init__(self, value):  
        self.value = value
        self.left = None
        self.right = None
  
#leaf nodes are at the very bottom of the branches
#depth of root node = 0, recursive or iterative

#time = O(n) where n= the number of nodes in the tree. traversing once though the tree
#space = RECURSIVE- O(h) where h is the height of the tree- recursive calls keep incrementing the call stack calls as you move down the tree - a balanced tree makes a difference becoause yo

#iterative
def nodeDepths(root):
    sum_depths = 0
    stack = [{"node": root, "depth" = 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sum_depths += depth
        stack.append({"node":node.left, "depth": depth +1})
        stack.append({"node":node.right, "depth": depth +1})
    return sum_depths

#recursive
def node(root, depth = 0):
    # handle Base Case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

#missed the python version    
//BST Branch Sum 

class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function branchSums(root) {
    const sums_list = []
    calculateBranch(root, 0, sums_list)
    return sums_list
}

function calculateBranch(node, branch_total, sums_list){
    const new_total = branch_total + node.value
    if (!node){
        return        
    }
    if(!node.left && !node.right){
        sums_list.push(new_total)
        return
    }
    calculateBranch(node.left, new_total, sums_list)
    calculateBranch(node.right,new_total,sums_list )
}

#BST Node Depths
the distance betweena node ina BT and the tree's root is called the nodes's depth

class BinaryTree:
    def __init__(self, value):  
        self.value = value
        self.left = None
        self.right = None
  
#leaf nodes are at the very bottom of the branches
#depth of root node = 0, recursive or iterative

#time = O(n) where n= the number of nodes in the tree. traversing once though the tree
#space = RECURSIVE- O(h) where h is the height of the tree- recursive calls keep incrementing the call stack calls as you move down the tree - a balanced tree makes a difference becoause yo

#iterative
def nodeDepths(root):
    sum_depths = 0
    #need to store all of the nodes and their depths
    stack = [{"node": root, "depth" = 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sum_depths += depth
        stack.append({"node":node.left, "depth": depth +1})
        stack.append({"node":node.right, "depth": depth +1})
    return sum_depths

#recursive
def node(root, depth = 0):
    # handle Base Case of recursion
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

#**********************Leetcode

# Remove Duplicates inplace 
def removeDuplicates(nums):
 
    if len(nums) == 0:
        return 0
    else:
        i = 0    
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]                
            else:
                i +=1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums)) 

#**********move zeros to end inplace 
def moveZeros(nums):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[i],nums[count] = nums[count], nums[i]
            count +=1            
    return nums

nums = [0,1,0,3,12]
print(moveZeros(nums))


# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.

def backspaceStrings(S,T):
    new_s = []
    new_t = []
    
    for i in range(0,len(S)):
        if S[i] != "#":
            new_s.append(S[i])
        else:
            if (len(new_s) > 0):
                new_s.pop()

    for i in range(0,len(T)):
        if T[i] != "#":
            new_t.append(T[i])
        else:
            if len(new_t) > 0:
                new_t.pop()
    
    return new_s == new_t

S = "a#c"
T = "a"

print(backspaceStrings(S,T))


#*************** Caesar cipher encryption
# - non empty lowercase string and a non-neg integer (k) , returns new string by shifting " wrapping " alphabet by k letters

# input - non-empty lowercase string IF NOT JUST LOWERCase do
 #       -  a uppercase list as well
# output - string lowercase - nonempty
# edgecase - really large k numbers, use the modulo to get the reamonder
# assumptions 

# O(n) linear time = iterating through the input string  and O(1) constant space even if you use the alpa array the arrya is only 26 letters long Constant,  if the alphabet aray was "n" letters then it would not be constant
# tests your use of the modulo operator

# We can know that this works for loop-arounds by observing the following behavior:
# 25%26=(0∗26+25)%26=25
# 26%26=(1∗26+0)%26=0
# 27%26=(1∗26+1)%26=1
# 28%26=(1∗26+2)%26=2
# and so on...

def swapLetters(string, key):
    alpha = list("abcdefghijklmnopqrstuvwxyz") 
    new_letters = []
    #index of a = 0, index of z = 25
    for letter in string:
        new_idx = (alpha.index(letter) + key) % len(alpha)
        new_letter = alpha[new_idx]
        print (f'New index for letter is {new_idx}, new letter is {new_letter}')
        new_letters.append(new_letter)
    return new_letters

string =  'xyz'
key = 1
print(swapLetters(string, key))

# ThreeNumberSum
# targetSum = find all triplets in the array that add up to the target sum
# numbers in acscending order and triplets in ascending order
# input = list and integer
# output = list of sub-arrays
# edgecase - if now numbers addup to target the return empty array
# assumptions - can assume non empty array of distict integers and an
#              integer representing the sum

#0(n^2) quadratic time  where n is the length of the array, need to iterate thur the for loop a and then we have to iterate thru again in the while loop.  0(n) linear - ome space usage beause if the sort and the storing of the triplets 
def threeNumberSum(sorted_nums, targetSum):
    #first sort the array so you can use left and right pointers
    sorted_nums.sort()
    print(sorted_nums)
    results = [] 
    #range -2 becuase we are always looking at 3 numbers at a time see line 21 
    for i in range(0,len(sorted_nums)-2):
        left = i + 1
        right = len(sorted_nums)-1
        while left < right:
            current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right] 
            if current_sum == targetSum:
                results.append([sorted_nums[i], sorted_nums[left],sorted_nums[right]])            
                left +=1            
                right -=1
            elif current_sum < targetSum:
                left +=1
            else:
                right-=1 
    return results

array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

print(threeNumberSum(array, target))


# *********************smallest difference
# input -  2 arrays - can be unequal length
# output - 1 array with 2 numbers number for first array in front
# edge case - 
# assumptions - 2 non-empty interger arrays only one pair will be correct answer

#O(n log(n) + m log(m)) when n = len of array1 and m = len of array2 - the arrays can be unequal in length - need to sort both arrays first and looping thru the first array  -linear quadratic time complexity 
#Space = O(1) - sorting arrays in place and the varaible we are are storing are constant space and array of the results (pair) and a diff sum -  nothing we are storing depends on the length of the arrays

# ask if you can sort the arrays in palce, if not you need to do do this:
#  a1_sorted = sorted(arrayOne)
#  a2_sorted = sorted(arayTwo) - this would take more space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    results = []
    a1_left = 0
    a2_left = 0  

    #this simplfies things because anything will be smaller that infinity
    #if gives you a starting point
    smallest_diff = float("inf")
    temp_diff = float("inf")
    #arrays can be unequal length
    while a1_left < len(arrayOne) and a2_left < len(arrayTwo):
        num1 = arrayOne[a1_left]
        num2 = arrayTwo[a2_left]
        #could do abs diff here but easier to read this way               
        if  num1 < num2:
            temp_diff = num2 - num1
            # #since our arrays are sorted and num1 is less than num2, if we move
            # to the mext number in array2 ( it is larger) so the diff would be #greater,so move to the next number in array1 and the diff might be
            # smaller
            #move to the next number in array1
            a1_left +=1
        elif num2 < num1:
            temp_diff = num1 - num2
            #move to the next number in array2
            a2_left+=1
        else:
            return [num1, num2]

        if temp_diff < smallest_diff:
            smallest_diff = temp_diff
            results = [num1,num2]

    return results
      
arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
print(smallestDifference(arrayOne, arrayTwo))



#****************************Binary tree example

# good sites:
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-index.php

# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

#Creating a tree with a single node.
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data


#   def PrintTree(self):
#         print(self.data)

# root = Node(10)
# root.PrintTree()

# # just like calling this
# def addNums(num1, num2):
#     total = num1 + num2
#     print(total)
# addNums(3,4)

# Inserting values into a BT
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()

#*********************Depth first search
# Node class with name and an array of optional children nodes.Implement the dpethfirstSearch method on the node class, which takes in an empty array , traverses the tree using the depth firs search (navigating from left to right)
#stores all of the nodes names in an input array and returns it

# graphs a collection of nodes that may or maynot be connected. the nodes are called vertices and the branches(connections) are called edges
#  Explore first left branch, as far down (deep as we can ), then go to the next branch to the right.

 #111 vertices in this graph and 10 edges
#  time complexity = O(v + e) - add every nodes name(v) we iterate throught the for loop for as may childresas the tree has so that is how many edges there are as well.
#Space- complexity is O(v) - length of the return array
class Node:
    #every Node has a name and an array of children nodes
    def __init__name(self, name):
        self.children = []
        self.name = name

    #can add a new child to the Node by appending a new Node to the children array
    def addChild(self,name):
        self.children.append(Node(name))

    def depthFirstSearch(self,array):
        #append to the array the nodes name
        array.append(self.name)
        #for every child in the children - call the depthFirst function on the child
        # and that will add the child name to the array
        for child in self.children:
            child.depthFirstSearch(array)
        return array

# ***************Find three largest numbers

# input - array of at least three integers
# output - array of threee intergers in sorted in acsending order
# edge cases
# assumptions - cannot sort array, there can be duplicate numbers

# time - O(n) linear  where n is the length of the array
# space - O(1) - constant just storing a larray of thre numbers
#need to keep track and store the three largest numbers
def findThreeLargestNumbers(array):
    largest = [None,None,None]
    for num in array:
        updateLargest(num, largest)
    return largest

#helper function is cleaner than doing everything in the for loop
def updateLargest(num,largest):
    #first see if we have a largest number 
    if largest[2] == None or num > largest[2]:        
        shiftAndUpdate(largest, num, 2)
    elif largest[1] == None or num > largest[1]:
        shiftAndUpdate(largest, num, 1)
    elif largest[0] == None or num > largest[0]:        
        shiftAndUpdate(largest, num, 0)
        

def shiftAndUpdate(array2, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array2[i] = num
        else:
            array2[i] = array2[i +1]

array = [141, 1, 17, -7]
print(findThreeLargestNumbers(array))

#*************************Selection sort
# going to create two sublists
# interate through list find the smallest number 
# and swap it it to the first sublist
# input - unsorted integer array
# output - sorted array
# edgecase
# assumptions

# time complexity = O(n^2)quardratic - where n is the
# length of the array need to traverse array multiple times
# to find the smallest number, the longer the array the longer it would take

# space complexity = O(1) constant - the swaps are in place and the solution
#  does not need additional storage or space is not dependent the length of the aray


def selectionSort(array):
    # starting index of sorted imaginary sublist
    current_idx = 0
    #keep going till you have sorted the
    # whole array- then the current-idx will equal the index of the last number in the array
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx +=1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j],array[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(array))