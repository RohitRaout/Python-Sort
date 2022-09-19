def InsertionSort(array):
    for i in range(1, len(array)):
  
        key_value = array[i]
        j = i-1
        while j >= 0 and key_value < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key_value
        print((array[j+1],array[i]))
 
array = [11, 10, 12, 4, 5]
print("The unsorted array: ", array)
InsertionSort(array)
print ("The sorted array using the Insertion Sort: ")
for i in range(len(array)):
    print (array[i])