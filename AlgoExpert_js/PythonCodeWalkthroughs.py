
    ##Insertion sort
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j-=1
    return array


array = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(array))





        









