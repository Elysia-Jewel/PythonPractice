def insert_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0:
            if lst[j+1] < lst[j]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
            j -= 1

    return lst

def insert_sort2(lst):
    for i in range(1, len(lst)):
        while i - 1 >= 0:
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
            i -= 1

    return lst

def insert_sort3(lst):
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

if __name__ == '__main__':
    test1 = [8,3,7,41,19,10]
    print('My algorithm: ', insert_sort3(test1[:]))
    print('Compare: ', sorted(test1))