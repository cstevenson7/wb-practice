
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
#Big O notation is O(log(n))
#                                                               
# arguments are: list of nums, the num we are trying to find, the start (aka index0) of the array, 
#                 and the end of the array (aka last index (len(array)-1)
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
Worst Case: O(n^2) Time - O(1) Space
#usually use a while loop ina bubble sort, best case for this type of sort would be linear O(n) -

#Helper function first
def swap(i,j,array):
    array[i], array[j] = array[j], array[i] # these are index umbersa
    
    
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
print
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