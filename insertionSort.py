#running time: O of n^2, ok for n < 30 or if you only need to run couple times overnight

myList = [5,10,4,7,6]
#index for the unsorted part of the array
for j in range(1,len(myList)):
    #1st element of the unsorted array
    key = myList[j]
    #last element of the sorted array
    i = j-1
    #if key value is less than than the last element of the sorted array, check the second to last element and so forth until the key is larger or we reached the beginning of sorted array
    while i >= 0 and key < myList[i]:
        #copy the value of the last element in sorted array to the next position, shifts by 1
        myList[i+1] = myList[i]
        i -= 1
    #assign key to the position 1 greater than i since i will represent the index of the last element smaller than key
    myList[i+1] = key