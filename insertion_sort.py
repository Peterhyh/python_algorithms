#Comparing numbers side by side from left to right and switching their index as needed

array_list = [2, 6, 5, 3, 7]


for i in range(1, len(array_list)):
    j = i 
    while array_list[j - 1] > array_list[j] and j > 0:
        array_list[j - 1], array_list[j] = array_list[j], array_list[j - 1]
        j -= 1

print(array_list)