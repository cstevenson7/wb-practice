
# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements.  
# You need to find the minimum number of swaps required to sort the array in ascending order.

# For example, given the array  we perform the following steps:



def minSwaps(arr):
    swaps = 0
    for i in range(0,len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            swaps +=1
            j-=1
    return swaps

print(minSwaps([4,3,1,2]))

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