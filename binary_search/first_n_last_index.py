# Prob- https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1?page=1&difficulty[]=-1&sortBy=submissions

# Given a sorted array arr containing n elements with possibly duplicate elements, 
# the task is to find indexes of first and last occurrences of an element x in the given array.
# n=9, x=5
# arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
# Output:  2 5
# TODO: Good question














def first_index(arr, n, x):
    l, r = 0 , n-1
    while l <= r:
        mid = (l + r) // 2
        if (mid == 0 or arr[mid - 1] != x ) and arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def last_index(arr, n, x):
    l, r = 0 , n-1
    while l <= r:
        mid = (l + r) // 2
        if (mid == n-1 or arr[mid + 1] != x)  and arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1

def find(arr,n,x):
    return [first_index(arr, n, x), last_index(arr, n, x)]