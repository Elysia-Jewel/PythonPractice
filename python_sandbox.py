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

string = "RDDDRDRRDR"
print(predictPartyVictory(string))