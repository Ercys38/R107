def selection_sort_verbose(lst):
    print(lst)
    for i in range(len(lst) - 1):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
        print(lst)

tab = [5, 2, 4, 8, 1, 3]

work = tab.copy()
selection_sort_verbose(work)

print(sorted(tab))
print(tab)

tab.sort()
print(tab)