from counting_sort import count_sort_place_digit

def radix_sort(lst, base):
    max_num = max(lst)
    exp = 0
    while max_num // (base ** exp) > 0:
        lst = count_sort_place_digit(lst, exp, base)
        exp += 1
    return lst

## Padding with special characters. Cons: additional complexity to evaluate paddings, additional complexity to remove paddings from strings after sorting
def radix_string(lst):

    return lst

## Without padding. Worst-case time complexity: O(N) where N is the sum of the characters of the strings in the list.
def radix_string_optimal(lst):
    #sort strings according to length
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0:
            if len(lst[j+1]) < len(lst[j]):
                lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1
    #radix sort from bottom up, skipping the strings after when first empty character is detected in a column

    return lst

if __name__ == '__main__':
    test1 = [8,3,7,41,19,10]
    test2 = [34, 85, 19, 74, 25]
    test3 = [200, 151, 291, 981, 369, 421, 671]
    test4 = ['dog', 'taro', 'cat', 'gudetama', 'elk'] #['cat', 'dog', 'elk', 'gudetama', 'taro']
    test5 = [170, 45, 75, 90, 802, 24, 2, 66]
    print('My algorithm: ', radix_string_optimal(test4[:]))
    print('Compare: ', sorted(test4))