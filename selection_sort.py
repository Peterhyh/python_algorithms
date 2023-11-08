# Setting a current minimum index
# For loop over the index numbers after the current minimum index to see if it is less than the current minimum index
# If it is, set the current minimum index number to new one
# Lastly, switch their index positions

arr = [2, 6, 5, 3, 7]

# for i in range(len(arr) - 1):
#     cur_min_idx = i
#     for j in range(i+1, len(arr)):
#         if arr[j] < arr[cur_min_idx]:
#             cur_min_idx = j
#     arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]


print(arr)
