# Comparing numbers side by side from left to right and switching their index as needed

arr = [2, 6, 5, 3, 7]


for i in range(1, len(arr)):
    j = i
    while arr[j - 1] > arr[j] and j > 0:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

print(arr)
