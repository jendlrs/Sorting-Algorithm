#Bubble Sort

#Step 1: Compare two adjacent elements at a time
#Step 2: Swap if the element in first index is greater than the second index. Else retain.
#Step 3: Repeat until there is no swap is required and all elements come to its correct position.

#Assigned the array values
numbers = [41, 4, 47, 94, 40, 66, 42, 23, 60, 55]

def bubble_sort(numbers):
    for i in range (len(numbers) - 1, 0, -1): #External loop
        for j in range(i): #internal loop
            if numbers[j]>numbers[j+1]:
                temp_num = numbers [j]
                numbers [j] = numbers[j+1]
                numbers [j+1] = temp_num

bubble_sort(numbers)
print(numbers)

