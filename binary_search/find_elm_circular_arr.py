# Search an element in a circularly sorted array
# Given a circularly sorted integer array, search an element in it. Assume there are no duplicates in the array,
#  and the rotation is in the anti-clockwise direction.
# https://www.techiedelight.com/search-element-circular-sorted-array/

# Input:
# nums = [8, 9, 10, 2, 5, 6]
# target = 10
# Output: Element found at index 2
# Input:
# nums = [9, 10, 2, 5, 6, 8]
# target = 5
# Output: Element found at index 3
 
 # nums = [8, 9, 10, 1, 2, 4, 5, 6, 7]

def search_pivot_ind(arr, t):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = l + r // 2
        prev, next = mid-1, mid+1
        if arr[mid] < arr[next] and arr[mid] < arr[prev]:
            return mid
        elif arr[mid] < arr[r]:
            r = mid - 1
        elif arr[mid] > arr[l]:
            l = mid + 1

        # elif arr[r] < t:
        #     r = mid - 1
        # else:
        #     l = mid + 1
        # print(mid, l, r)
    return -1  
# [8, 9, 10, 1, 2]
arr, t = [8, 9, 10, 1, 2, 4, 5, 6, 7], 10

print(search_pivot_ind(arr, t))
