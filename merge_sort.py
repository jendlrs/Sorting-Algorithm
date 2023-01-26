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

        print (left_array)
        print (right_array)

merge_sort(numbers) #call the function