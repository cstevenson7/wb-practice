# Algo Strategy:


# If the given input is sorted (array, list, or matrix), then we will use a variation of Binary Search or a Two Pointers strategy.

# If we’re dealing with top/maximum/minimum/closest k elements among n elements, we will use a Heap.

# If we need to try all combinations (or permutations) of the input, we can either use recursive Backtracking or iterative Breadth-First Search.

# Following this pattern-based approach helped me save a lot of preparation time. Once you’re familiar with a pattern, you’ll be able to solve dozens of problems with it. In addition, this strategy made me confident to tackle unknown problems, as I’ve been practicing mapping unknown problems to known ones.







# #*********************Binary Search Practice
# #Big O notation is O(log(n))
# # If all the names in the world are written down together in order and you want to search for the position of a specific name, binary search will accomplish this in a maximum of 35 iterations.

# # Binary search works only on a SORTED SET of elements. To use binary search on a collection, the collection must first be sorted.

# def binarySearchHelper(array, target ,left,right):
#     while left <= right: # when the left "bound" is less than the right "bound" we have searched the whole array
#         middle = (left + right)//2
#         potentialMatch = array[middle]  # here we are putting in the number not the index

#         if target == potentialMatch:
#             #as soon as we have found it break out of the loop
#             return print(f"We have a match at index {middle}")
#         elif target < potentialMatch: # target is less than the middle index number
#             #middle is the index of the mid number# - step back and split again
#             right = middle - 1  
#         else:
#             # the target is greater the the middle index num so move one index to the right and split again                                               
#             left = middle + 1 
#     # one we are dumped out of the while loop we have searched the whole loop and have no found a match
#     return -1   

# def binarySearch(array, target):
#     arr2 = sorted(array)
#     return binarySearchHelper(arr2, target,0,len(array)-1) 

# target = 23
# array = [1,4,7,9,12,22,23]
# print(binarySearch(array, target))




#************************** recursive factorial function Week3-day2***************
# this is 5! = 5 * 4 * 3 * 2 * 1

#This starts at 5, then goes down the stack  until 1(or2?) then starts multiplying the values to itself up the stack

     





#******************* Recursive fibonnaci functionWeek3 -day2*********************

 








#*************************************** Linked Lists

#**good atricle arrays vs linked lists
#https://www.geeksforgeeks.org/linked-list-vs-array/

# So Linked list provides the following two advantages over arrays
# 1) Dynamic size
# 2) Ease of insertion/deletion

# Linked lists have following drawbacks:
# 1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do a binary search with linked lists.
# 2) Extra memory space for a pointer is required with each element of the list.
# 3) Arrays have better cache locality that can make a pretty big difference in performance.

# The medium example
# //https://medium.com/outco/reversing-a-linked-list-easy-as-1-2-3-560fbffe2088

# What I want to demonstrate with this post, is a simple way of reversing a list, with just 3 pointers. This runs in O(N) time and O(1) space.

# initializeing an empty linked list
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #Create and Connect the nodes with the class above
# five = ListNode(5)
# four = ListNode(4, five)
# three = ListNode(3, four)
# two = ListNode(2, three)
# one = ListNode(1, two)


# function reverse(head) {
# # // Step 1 nitially, we want both the current and the following equal to the head that is given as the input.
# # This is because we can’t assume the length of the linked list. What if head was null and we’re looking at an empty list?
#   let previous = null
#   let current = head
#   let following = head
# #   The third step is to figure out the order of operations so we don’t lose track of anything.
# # That while loop we just made won’t run unless we have at least one node. But once it does, the first thing we want to do is set following to following.next so we don’t lose track of what comes after current .
# # # Eventually though, it will reach the last node’s next, which ALWAYS points to null Eventually though, it will reach the last node’s next, which ALWAYS points to null 
#   while(current !== null) {
#     following = following.next
#     current.next = previous
#     previous = current          
#     current = following
#   }
# // Step 3  
#   return previous
# }




# # thsi is wwhat  Brian had to create the linked list
# initializeing an empty linked list
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #Create and Connect the nodes with the class above
# five = ListNode(5)
# four = ListNode(4, five)
# three = ListNode(3, four)
# two = ListNode(2, three)
# one = ListNode(1, two)

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
    
# print(reverseList(one))


# #****************************another example
# https://www.geeksforgeeks.org/reverse-a-linked-list/
# # Python program to reverse a linked list  
# # Time Complexity : O(n) 
# # Space Complexity : O(1) 
  
# # Node class  
# class Node: 
  
#     # Constructor to initialize the node object 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None
  
# class LinkedList: 
  
#     # Function to initialize head 
#     def __init__(self): 
#         self.head = None
  
#     # Function to reverse the linked list 
#     def reverse(self): 
#         prev = None
#         current = self.head 
#         while(current is not None): 
#             next = current.next
#             current.next = prev 
#             prev = current 
#             current = next
#         self.head = prev 
          
#     # Function to insert a new node at the beginning 
#     def push(self, new_data): 
#         new_node = Node(new_data) 
#         new_node.next = self.head 
#         self.head = new_node 
  
#     # Utility function to print the linked LinkedList 
#     def printList(self): 
#         temp = self.head 
#         while(temp): 
#             print temp.data, 
#             temp = temp.next
  
  
# # Driver program to test above functions 
# llist = LinkedList() 
# llist.push(20) 
# llist.push(4) 
# llist.push(15) 
# llist.push(85) 
  
# print "Given Linked List"
# llist.printList() 
# llist.reverse() 
# print "\nReversed Linked List"
# llist.printList() 
  
# #*****Given below is the implementation of a standard class-based singly Linked List in Python.
# https://www.educative.io/edpresso/how-to-reverse-a-linked-list-in-python

# # A single node of a singly Linked List
# class Node:
#   # constructor
#   def __init__(self, data = None, next=None): 
#     self.data = data
#     self.next = next

# # A Linked List class with a single head node
# class LinkedList:
#   def __init__(self):  
#     self.head = None
  
#   # insertion method for the linked list
#   def insert(self, data):
#     newNode = Node(data)
#     if(self.head):
#       current = self.head
#       while(current.next):
#         current = current.next
#       current.next = newNode
#     else:
#       self.head = newNode
  
#   # print method for the linked list
#   def printLL(self):
#     current = self.head
#     while(current):
#       print(current.data)
#       current = current.next

# # Singly Linked List with insertion and print methods
# LL = LinkedList()
# LL.insert(3)
# LL.insert(4)
# LL.insert(5)
# LL.printLL()



# ****************Given below is an iterative approach as to how you can reverse a given Linked List in Python:
#https://www.educative.io/edpresso/how-to-reverse-a-linked-list-in-python
# Initialize variables:
# previous: Initially pointing at None (line 3), this variable points to the previous element so the node.next link can be reversed using it (line 9). This is then updated to the node next to it, i.e., current (line 10).

# current: Initially pointing to head (line 4), the node being pointed to by this variable gets its node.next set to the previous item in the list (line 9). This is then updated to the node next to it,​ i.e., following (line 11).

# following: Initially pointing to the second node (line 5), this is used so the current pointer may move one step ahead (line 12-13) in each iteration. 

#************************************************
#In leetcode  the -> means it expects NO RETURN
#def moveZeroes(self, nums: List[int]) -> None: 


# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# def moveZeros(nums):
#   for n in nums:
#     if n == 0:
#       t = nums.pop(nums.index(n))
#       nums.append(t)
#   return nums


# nums = [0,1,0,3,12]
# #Output: [1,3,12,0,0]

# print(moveZeros(nums))

# Brians Solution

#  i = index
# def moveZeros(nums):
#   counter  = 0

  #Counting the non-zeros
#   for i in range (len(nums)):
#     if nums[i] != 0:
#       nums[counter] =  nums[i]
#       counter +=1

#    # fill rest with zeros
#   while counter < len(nums):
#     nums[counter] = 0
#     counter +=1
#   return nums

# nums = [0,1,0,3,12]
# print(moveZeros(nums))

#***************** Some WB Question?

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15


# def subtractProductAndSum(num):
#     new_num = str(num)
#     prod = 1
#     sum = 0
#     for x in new_num: 
#       prod = prod * int(x)
#       sum = sum + int(x)
#     return prod - sum

# n = 4421
# print(subtractProductAndSum(n))

# # JoSHES ANSWER?
# def subtractProductAndSum(num):
#     prod = 1
#     sum1 = 0
#     while num > 0:
#         n = num % 10
#         prod *= n
#         sum1 += n
#         num = num // 10
#     return prod-sum1


#******************Insertion Sort Worst Case: O(n^2) time - O(1)space


# also a swapping sort,  this inserts the values in its correct place instead of keeping it bubbling up

# #Helper function first
# def swap(i,j,array):
#     array[i], array[j] = array[j], array[i] 
    
# def insertionSort(array):
#     #Not -1   start at index1 (lookin at the vaue first NEXT to the first number
#     #  and using the length of the array -  not the index number
#     #  in the array this time going past the array 
#     for i in range(1,len(array)):       
#         j = i  #pointer as a place holder not that can increment backwards
#         while j > 0 and array[j] < array[j-1]:   #looking backward
#             swap(j, j-1, array)
#             j-=1
#     return array
# print
# print(insertionSort([10,50,30,2,1]))





def helper(i,j,array):
    array[i], array[j] = array[j], array[i]
    return array

def insertionSort(array):
    #always looks at the value behind
    #NOT USING I AS AN index , only a counter
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
        # then we need to swap
            helper( j,j-1, array,)
            j-=1

    return array

print(insertionSort([10,50,99,30,2,1]))
    




#***************merge Sort
# step1: Sptint everything into its own group
# step2 From left to right merge two groups together
# step3 while merging place each item in the correct position with in the merged group
# step4 Contine steps 3-4 until one group is left

from random import randint
#used to genetate list of 5 numbers from 0 - 20

nums = [randint(0,20) for i in range(5)]

#write merge sort below
def mergeSort(alist):
    print("Splitting...", alist)
    # Step1: Divide and conquer divide into two listts into 2 equal halves until both have a length of 1
    if len(alist) > 1:
        mid = len(alist) // 2 # no remainder do one half would be 2 one would be two This is the midpoint of the array
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf) # keep splitting until we get to a list witha length of one. Do lefthalf first , 
        mergeSort(righthalf) # then do the righthalf 
        
        #index pointers for our list
        i = 0
        j = 0
        k = 0
        
        #Step2 Compare lefthalf  and righthalf 
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:   #this is where  we start comapring numbers
                alist[k] = lefthalf[i]
                i = i + 1    #increment and start process all over again           
            else:
                alist[k] = righthalf[j]
                j = j + 1            
            k = k + 1
            
        #Step3
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    
    print("Merging: ", alist)  
    return alist
            
mergeSort(nums)   




# #******************bubble Sort
# def bubbleSort(array):
#     #Flag or pointer to confim sort
#     isSorted = False
#     while not isSorted:  #This means while Is sorted is True , but we cant; use it here# we need to go through this loop at least once to se if the list is sorted      
#         isSorted = True   # we need this to catch when the array has been sorted. See comments below
#         for num in range(len(array)-1):   #num is index and len(array)-1 is the last index number
#             if array[num] > array[num+1]:
#                 swap(num, num+1, array)
#                 isSorted = False
#     return array




If the given input is sorted (array, list, or matrix), then we will use a variation of Binary Search or a Two Pointers strategy.