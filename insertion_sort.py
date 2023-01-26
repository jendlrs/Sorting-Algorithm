#Insertion Sort

#Step 1: Divide the array into two parts: sorted and unsorted. For the first iteration, only the first element is in the sorted part
#Step 2: Get the first element in the unsorted part, then compare the values, and insert the element in its proper position
#Step 3: Repeat until all the numbers are in the sorted part.

#Assigned the array values
numbers = [41, 4, 47, 94, 40, 66, 42, 23, 60, 55]

def insertion_sort (numbers):
    for i in range(1, len(numbers)): #Outer loop that will iterate the unsorted part of the list
        for j in range (i-1, -1, -1): #Inner loop that will cover the sorted part
            if numbers [j] > numbers [j+1]:
                numbers [j], numbers [j+1] = numbers [j+1], numbers [j] #Swap to move the element in correct position
            else:
                break

insertion_sort(numbers)
print (numbers)