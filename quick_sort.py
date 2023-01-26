#Quick Sort 

#Step 1: Choose a pivot element (usually last or random)
#Step 2: Stores elements less than pivot in left subarray
       # Stores elements less than pivot in right subarray
#Step 3: Call quick sort recursively on left subarray
       # Call quick sort recursively on left subarray
#Step 4: Repeat until all the elements come to its correct position.

#Assigned the array values
numbers = [41, 4, 47, 94, 40, 66, 42, 23, 60, 55]

def quick_sort (numbers, left, right):
    if left < right:
        partition_pos = partition (numbers, left, right)
        
        #Recursion of sorting two arrays
        quick_sort (numbers, left, partition_pos - 1) #From leftmost index to the number before index partition
        quick_sort (numbers, partition_pos + 1, right) #From the number after the partition to the rightmost index.

def partition(numbers, left, right):
    i = left
    j = right - 1
    pivot = numbers[right]

    while i < j:
        #Moving i to the right
        while i < right and numbers [i] < pivot:
            i += 1
        #Moving j to the left
        while j > left and numbers [j] >= pivot:
            j -= 1

        if i < j: #Check if two elements (i and j) didn't cross, then swap elements at index i with the element at index j
            numbers[i], numbers[j] = numbers[j], numbers[i] 

    if numbers [i] > pivot: #Check if two elements (i and j) have crossed, then swap array at index i with the array at index right
        numbers [i], numbers [right] = numbers [right], numbers [i]
    
    return i

quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
