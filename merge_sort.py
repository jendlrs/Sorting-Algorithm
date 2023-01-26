#Merge Sort

#Step 1: Divide array in half
#Step 2: Call the merge sort for each half to sort them
#Step 3: Merge both sorted halves to have one sorted array

#Assigned the array values
numbers = [41, 4, 47, 94, 40, 66, 42, 23, 60, 55]

def merge_sort (numbers):
    if len(numbers) > 1: #Split whole array in half
        left_array  = numbers [:len(numbers)//2] #Sub array for first half (left to middle)
        right_array =  numbers [len(numbers)//2:] #Sub array for second half (middle to last)

        #recursion for two array
        merge_sort(left_array)
        merge_sort(right_array)

        #Implement the merge step
        i = 0 #leftmost element of the left array
        j = 0 #leftmost element of the right array

merge_sort(numbers) #call the function