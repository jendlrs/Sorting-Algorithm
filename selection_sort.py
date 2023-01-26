#Selection Sort

#Step 1: Find the smallest element in the array
#Step 2: Swap where the search started 
#Step 3: Repeat until all the elements come to its correct position.

#Assigned the array values
numbers = [41, 4, 47, 94, 40, 66, 42, 23, 60, 55]
print (f"\nThe unsorted numbers: {numbers}")

def selection_sort (numbers): #This will check every value in the array
    for i in range (0, len(numbers) - 1): 
        current_min_index = i 
        for j in range (i + 1, len (numbers)):
            if numbers[j] < numbers [current_min_index]: 
                current_min_index = j #changed the minimum index once the element that is lower than the current min index was detected.

        numbers [i], numbers[current_min_index] = numbers[current_min_index], numbers[i] #Swap the element where the search started

selection_sort(numbers) #call the funtion
print(f"\nThe sorted numbers: {numbers}\n")
