def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for idx in range(i+1, len(lst)):
            if lst[idx] < lst[min]:
                min = idx
        lst[i], lst[min] = lst[min], lst[i]
    
    return lst

if __name__ == "__main__":
    lst = [8,3,7,41,19,10]
    sorted = selection_sort(lst[:])
    print(sorted)
