# Divide and conquer algorithm
# Make the pivot the last index number
# Create 2 variables: i and j
# i will iterate from left to right to find the numbers bigger than pivot
# j will iterate from right to left to find the numbers smaller than the pivot
# Once j passes i, swap i with pivot


def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        # calling quicksort on all elements that are less then the pivot element
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


# returns the index of the pivot element after the first step of quicksort
def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]


quicksort(arr, 0, len(arr) - 1)
print(arr)
