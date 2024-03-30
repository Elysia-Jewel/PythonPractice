## Counting sort only works for single digit numbers.
def count_sort(lst):
    #find max
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    #build freq. table
    table = [0] * (max_num + 1)
    #update freq. table
    for num in lst:
        table[num] += 1
    #sort array
    i = 0
    for idx in range(len(table)):
        freq = table[idx]
        while freq > 0:
            lst[i] = idx
            freq -= 1
            i += 1

    return lst

## Stable version of counting sort.
def count_sort_stable(lst):
    #get max
    max_num = 0
    for i in lst:
        if i > max_num:
            max_num = i
    #build count array
    count_array = [[] for _ in range(max_num + 1)]
    #update count array
    for i in lst:
        count_array[i].append(i)
    #build sorted array
    output = []
    for i in count_array:
        output += i

    return output

## Stable version of counting sort. Receives multi-digit numbers and works on 
## a specific place digit.
def count_sort_place_digit(lst, exp, base):
    #build count array
    count_array = [[] for _ in range(base)]
    #update count array according to digit in specified place value
    for item in lst:
        digit_to_count = item // (base ** exp) % base
        count_array[digit_to_count].append(item)
    #build sorted array
    output = []
    for i in count_array:
        output += i
    return output

if __name__ == '__main__':
    test1 = [5, 3, 9, 1, 5, 3, 0] #[0, 1, 3, 3, 5, 5, 9]
    extreme1 = []
    test2 = [34, 85, 19, 74, 25]
    print('My algorithm: ', count_sort_place_digit(test2[:], 0, 10))
    #print('Compare: ', sorted(test1))