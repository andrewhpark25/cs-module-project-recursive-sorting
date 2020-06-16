# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
  
    # Base case: while start and end don't overlap
    while start < end:
        # Check midpoint
        mid = (start + end) // 2
    # Return true if equal
        if arr[mid] == target:
            return mid
    # Else, if target is smaller than mid, it should be in left subarray
        elif target < arr[mid]:
             return binary_search(arr, target, start, mid) 
    # Else, if target is bigger than mid, it should be in right subarray
        else:
             return binary_search(arr, target, mid + 1, end) 

    return -1  # not found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#def agnostic_binary_search(arr, target):
    # Your code here

