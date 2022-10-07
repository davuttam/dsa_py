# Question 1
# Implement the function is_sorted(array) which returns true if the specified array is sorted, and false if not.

def is_sorted(array):
    for ind in range(0, len(array)-1):
        if array[ind] > array[ind+1]:
            return False
    return True

array = [1,5,3,4,2]
result = is_sorted(array)
print("Result is ", result)