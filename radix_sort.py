from counting_sort import count_sort_place_digit

def radix_sort(lst, base):
    max_num = max(lst)
    exp = 0
    while max_num // (base ** exp) > 0:
        lst = count_sort_place_digit(lst, exp, base)
        exp += 1
    return lst

def radix_string(lst):
    return lst

def radix_string_unequal(lst):
    return lst

if __name__ == '__main__':
    test1 = [8,3,7,41,19,10]
    test2 = [34, 85, 19, 74, 25]
    test3 = [200, 151, 291, 981, 369, 421, 671]
    print('My algorithm: ', radix_sort(test3[:], 10))
    print('Compare: ', sorted(test3))