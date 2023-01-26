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
        quick_sort (numbers, left, partition_pos -1)
        quick_sort (numbers, partition_pos + 1, right)

def partition(numbers, left, right):