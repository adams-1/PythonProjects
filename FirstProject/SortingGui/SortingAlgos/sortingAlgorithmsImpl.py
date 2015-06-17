__author__ = 'rage'

def selectionSort(arr):

    minIndex = 0

    for i in range(0,len(arr) ):
        minIndex = i

        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]



def insertionSort(arr):

    val = 0

    for i in range(1, len(arr)):

        val = arr[i]

        j = i - 1
        while( j >= 0 and arr[j] >= val):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = val



arr = [3,4,2,6,1]
insertionSort(arr)
print (arr)
