#Out-of-place variant
def quick_sort1(lst):
    pivot_pos = len(lst) // 2

    if pivot_pos > 0: #can still be divided into left & right
        left = []
        right = []
        for i in range(pivot_pos):
            if lst[i] <= lst[pivot_pos]:
                left.append(lst[i])
            else:
                right.append(lst[i])
        for i in range(pivot_pos+1, len(lst)):
            if lst[i] <= lst[pivot_pos]:
                left.append(lst[i])
            else:
                right.append(lst[i])
        return quick_sort1(left) + [lst[pivot_pos]] + quick_sort1(right)
    else:
        return lst

#Hoare's variant
#Lomuto's variant

if __name__ == '__main__':
    print("-" * 10, "TEST CASES", "-"*10)
    test1 = [8,3,7,41,19,10]
    test2 = [0, 2, 1, 0, 2, 1, 2, 0]
    print('My algorithm: ', quick_sort1(test1[:]))
    print('Compare: ', sorted(test1))

    #time complexity
    print("-" * 10, "TIME COMPLEXITY", "-"*10)
    from timeit import timeit
    stmt = 'quick_sort1(test1[:])'
    setup = '''
from __main__ import quick_sort1
from __main__ import test1'''
    print("Execution time:", stmt, timeit(stmt, setup, number=100000))

    #space complexity
    print("-" * 10, "SPACE COMPLEXITY", "-"*10)
    from tracemalloc import start, stop, get_traced_memory
    start()
    quick_sort1(test1[:])
    print(get_traced_memory())
    stop()
