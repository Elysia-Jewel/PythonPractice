#myList = [8,3,7,41,19,10]

def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i -1
        while j >= 0 and lst[i] < lst[j]:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1

def counting_sort(lst):
    #find max
    max = lst[0]
    for item in lst:
        if item > max:
            max = item
    #build count-array
    count_array = [0] * (max + 1)
    #update count-array
    for item in lst:
        count_array[item] += 1
    #rebuild array, but sorted
    lst_pos = 0
    for idx in range(len(count_array)):
        freq = count_array[idx]
        for _ in range(freq):
            lst[lst_pos] = idx
            lst_pos += 1
    return lst

#base-10
# def radix_sort(lst):
#     #find max length of number
#     max = 0
#     for idx in range(len(lst)):
#         length = len(str(lst[idx]))
#         if length > max:
#             max = length

#     #repeat for k number of times
#     for i in range(max):
#         #counting sort to compare
#             #build count-array
#         count_array = [[] for i in range(10)]
#             #update count-array
#         for item in lst:
#             #extract digit
#             digit = (item // (10**i)) % 10
#             count_array[digit].append(item)
#             #rebuild array as sorted
#             tmp = []
#         for i in range(len(count_array)):
#             tmp += count_array[i]
#         lst = tmp
#     return lst

def counting_sort(lst, exp):
    n = len(lst)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (lst[i] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (lst[i] // exp) % 10
        output[count[index] - 1] = lst[i]
        count[index] -= 1
        i -= 1
    
    return output

def radix_sort(lst):
    max_val = max(lst)
    exp = 1

    while max_val // exp > 0:
        lst = counting_sort(lst, exp)
        exp *= 10

    return lst

# Example usage:
lst = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_lst = radix_sort(lst[:])
print("Sorted list:", sorted_lst)

def radix_10():
    return

def radix_2():
    return

def radix_32():
    return

def radix_left():
    return

def radix_right():
    return

# myList = [200, 151, 291, 981, 369, 421, 671]
# x = radix_sort(myList[:])
# print(myList)
# print(x)