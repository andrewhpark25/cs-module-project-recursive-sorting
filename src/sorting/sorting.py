# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    a = 0
    b = 0
    
    while a < len(arrA) and b < len(arrB):
        #compare elements that a and b point at 
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
        # add elements from other list
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1
             
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
   # break array down recursively when list goes down to length of 1
    if len(arr) > 1:
       left = merge_sort(arr[:len(arr) // 2])
       right = merge_sort(arr[len(arr) // 2:])
       arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here