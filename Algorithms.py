import math
# Algorithm of Selection Sort


class sort:
    def SelectionSort(csvData,arr): 
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
            csvData.row[i], csvData.row[min] = csvData.row[min], csvData.row[i]
        return csvData

    # Algorithm of Insertion Sort
    def insertionSort(csvData, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            csvDataList = csvData.row[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                csvData.row[j+1] = csvData.row[j]
                arr[j+1] = arr[j]
                j = j-1
            arr[j+1] = key
            csvData.row[j+1] = csvDataList
        return csvData

    # Algorithm of Bubble Sort
    def BubbleSort(csvData, arr):
        for i in range(len(arr)):
            flag = False
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    csvData.row[j], csvData.row[j+1] = csvData.row[j+1], csvData.row[j]
                    flag = True
            if flag == False:
                break
        return csvData

    # Algorithm of Merge Sort
    def mergeSort(csvData, arr):
        if len(arr) > 1:
            mid = math.ceil(len(arr)/2)
            left = arr[:mid]
            csvLeft = csvData.row[:mid]
            right = arr[mid:]
            csvRight = csvData.row[mid:]
            sort.mergeSort(csvLeft, left)
            sort.mergeSort(csvRight, right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    csvData.row[k] = csvLeft[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    csvData.row[k] = csvRight[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                csvData.row[k] = csvLeft[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                csvData.row[k] = csvRight[j]
                j += 1
                k += 1
        return csvData

    # Algorithm of Quick Sort

    def quickSort(csvData, arr, low, high):
        if len(arr) == 1:
            # return arr
            return csvData
        if low < high:

            pi = sort.partition(csvData, arr, low, high)

            sort.quickSort(csvData, arr, low, pi-1)
            sort.quickSort(csvData, arr, pi+1, high)
        return csvData

    def partition(csvData, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                csvData.row[i], csvData.row[j] = csvData.row[j], csvData.row[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        csvData.row[i+1], csvData.row[high] = csvData.row[high], csvData.row[i+1]
        return (i+1)

    # Algorithm of Radix Sort
    def countingSort(csvData, arr, exp):

        count = [0 for x in range(10)]
        # result = [0 for y in range(len(arr))]

        for i in range(0, len(arr)):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i-1]

        for i in range(len(arr)-1, -1, -1):
            index = arr[i] // exp
            csvData.row[count[index % 10] - 1] = csvData.row[i]
            count[index % 10] -= 1

        # for j in range(0, len(arr)):
        #     arr[j] = result[j]

    def RadixSort(csvData, arr):
        max_num = max(arr)
        exp = 1
        while max_num / exp > 0:
            sort.countingSort(csvData, arr, exp)
            exp *= 10
        return csvData

    # Algorithm of Bucket Sort

    def bucketSort(csvData, array):
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
            return 

    # Algorithm of Counting Sort
    def CountingSort(csvData, arr):
        max_num = max(arr)
        min_num = min(arr)
        k = max_num - min_num + 1

        count = [0 for x in range(k)]
        # csvData.row = [0 for y in range(len(arr))]

        for i in range(0, len(arr)):
            count[arr[i]-min_num] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for i in range(len(arr)-1, -1, -1):
            csvData.row[count[arr[i] - min_num] - 1] = csvData.row[i]
            count[arr[i] - min_num] -= 1

        return csvData

    # Algorithm of Tim Sort
    MINIMUM= 32
  
    def find_minrun(n): 
        r = 0
        while n >= sort.MINIMUM: 
            r |= n & 1
            n >>= 1
        return n + r 
    
    def insertion_sort(array, left, right): 
        for i in range(left+1,right+1):
            element = array[i]
            j = i-1
            while element<array[j] and j>=left :
                array[j+1] = array[j]
                j -= 1
            array[j+1] = element
        return array
                
    def merge(array, l, m, r): 
    
        array_length1= m - l + 1
        array_length2 = r - m 
        left = []
        right = []
        for i in range(0, array_length1): 
            left.append(array[l + i]) 
        for i in range(0, array_length2): 
            right.append(array[m + 1 + i]) 
    
        i=0
        j=0
        k=l
    
        while j < array_length2 and  i < array_length1: 
            if left[i] <= right[j]: 
                array[k] = left[i] 
                i += 1
    
            else: 
                array[k] = right[j] 
                j += 1
    
            k += 1
    
        while i < array_length1: 
            array[k] = left[i] 
            k += 1
            i += 1
    
        while j < array_length2: 
            array[k] = right[j] 
            k += 1
            j += 1
    
    def timSort(array): 
        n = len(array) 
        minrun = sort.find_minrun(n) 
    
        for start in range(0, n, minrun): 
            end = min(start + minrun - 1, n - 1) 
            sort.insertion_sort(array, start, end) 
    
        size = minrun 
        while size < n: 
    
            for left in range(0, n, 2 * size): 
    
                mid = min(n - 1, left + size - 1) 
                right = min((left + 2 * size - 1), (n - 1)) 
                sort.merge(array, left, mid, right) 
    
            size = 2 * size 

        return array