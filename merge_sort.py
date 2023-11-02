#Divide and conquer method
arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]


def merge_sort(arr):
    if len(arr) > 1:                                                            # 1) Check if the lenght of array is less more than 1
        left_arr = arr[:len(arr)//2]                                            # 2) Split the array in half
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)                                                    
        merge_sort(right_arr)
    
        left_idx = 0                                                            # 3) Keeping track of index numnbers
        right_idx = 0
        merged_idx = 0

        while left_idx < len(left_arr) and right_idx < len(right_arr):          # 4) Enter loop if left index number is lower than length of left array AND same with the right side
            if left_arr[left_idx] < right_arr[right_idx]:                       # 5) If the first number in the left array is less than the first right number, make the first number in the merged array equals to the left first number
                arr[merged_idx] = left_arr[left_idx]
                left_idx += 1
            else:                                                               # 6) If the first number in the right array is less than the first left number, make the first number in the merged array equals to the right first number
                arr[merged_idx] = right_arr[right_idx]
                right_idx += 1

            merged_idx += 1
        
        while left_idx < len(left_arr):                                         # 7) Adding the leftovers from either side towards the end of the merged array
            arr[merged_idx] = left_arr[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right_arr):
            arr[merged_idx] =right_arr[right_idx]
            right_idx += 1
            merged_idx += 1

merge_sort(arr)
