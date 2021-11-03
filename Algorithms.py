import math
#Algorithm of Selection Sort
def SelectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j   
        arr[i], arr[min] = arr[min], arr[i]

#Algorithm of Insertion Sort
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

#Algorithm of Bubble Sort
def BubbleSort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            break

#Algorithm of Merge Sort
def mergeSort(arr):
    if len(arr) > 1:
        mid = math.ceil(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


#Algorithm of Quick Sort
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr, low, high):
    i = (low-1)      
    pivot = arr[high]    

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

#Algorithm of Radix Sort
#Algorithm of Bucket Sort
def bucketSort(array):
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    print(array)

#Algorithm of Counting Sort
def CountingSort(arr):
    max_num = max(arr)
    min_num = min(arr)
    k = max_num - min_num + 1

    count = [0 for x in range(k)]
    output = [0 for y in range(len(arr))]
 

    for i in range(0, len(arr)):
        count[arr[i]-min_num] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - min_num] - 1] = arr[i]
        count[arr[i] - min_num] -= 1
 
    return output


#Algorithm of Tim Sort