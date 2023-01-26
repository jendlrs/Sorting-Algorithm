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
        k = 0 #merged array index

        #Comparing
        while i < len(left_array) and j < len (right_array):
            if left_array [i] < right_array [j]:
                numbers[k] = left_array[i]

                i +=1
                k +=1
            else:
                numbers [k] = right_array[j]
                j +=1
                k +=1

        while i < len(left_array): #Transfer every element from left array to the merge array without getting into right array
            numbers [k] = left_array[i]
            i +=1
            k +=1

        while j < len (right_array): #Transfers elements from right array to the merged array
            numbers [k] = right_array[j]
            j +=1
            k +=1


merge_sort(numbers) #call the function
print (numbers)