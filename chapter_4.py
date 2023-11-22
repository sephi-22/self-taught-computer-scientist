# Implement bubble sort.
def bubble_sort(lista):
    loop_count = 0
    for i in range(0, len(lista)):
        swapped = 0
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                j += 1
                swapped = 1
                loop_count += 1
        if swapped == 0:
            print("Done after loops:", loop_count)
            break
    return lista


myList = [23, 2, 52, 63, 46, 42, 12]
myList2 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
print(bubble_sort(myList))
print(bubble_sort(myList2))


# Book's version of bubble_sort
def bubble_sort_book(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


myList = [23, 2, 52, 63, 46, 42, 12]
print(bubble_sort_book(myList))

# We can also improve this bubble sort by adding i to the second for loop. In this case, we don't need to compare the
# last element in the first loop, the second to last and last element in the second loop, and so on.


def bubble_sort_book_optimization_1(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list


myList = [23, 2, 52, 63, 46, 42, 12]
print(bubble_sort_book_optimization_1(myList))

# We can optimize this further by adding a check to see if elements were swapped. If no elements were swapped, we can end this early


def bubble_sort_book_optimization_2(a_list):
    list_length = len(a_list) - 1
    for i in range(list_length):
        swap_flag = False
        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                swap_flag = True
        if swap_flag == False:
            return a_list
    return a_list


myList = [23, 2, 52, 63, 46, 42, 12]
print(bubble_sort_book_optimization_2(myList))


# Insertion sort based on my knowledge after reading the explanation in book.
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i - 1]
            i -= 1
        a_list[i] = value
    return a_list


myList = [23, 2, 52, 63, 46, 42, 12]
print("MyList is", myList)
print(insertion_sort(myList))


# This is how to implement merge sort in python.
def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_half[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_half):
            a_list[alist_ind] = left_half[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1


myList = [23, 2, 52, 63, 46, 42, 12]
print("MyList is", myList)
merge_sort(myList)
print(myList)

# Using python's own functions.
print("Using sorted")
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list))
print(a_list)

print("Using sorted with words")
a_list = ["Guido van Rossum", "James Gosling", "Brendan Eich", "Yukihiro Matsumoto"]
print(sorted(a_list))
print(a_list)

print("Using sorted with descending order")
a_list = [1, 8, 10, 33, 4, 103]
print(sorted(a_list, reverse=True))
print(a_list)

print("Using sorted with key (len)")
a_list = ["onehundred", "five", "seventy", "two"]
print(sorted(a_list, key=len))
print(a_list)

print("Using sort instead of sorted")
a_list = [1, 8, 10, 33, 4, 103]
print("A list before sort is", a_list)
a_list.sort()
print("A list after sort is", a_list)


# Quicksort (uses random pivot)
def quicksort(list_a):
    if len(list_a) < 2:
        return list_a  # Base Case
    else:
        pivot = list_a[len(list_a) // 2]  # Choosing a pivot
        left = [i for i in list_a if i < pivot]
        middle = [i for i in list_a if i == pivot]
        right = [i for i in list_a if i > pivot]
        return quicksort(left) + middle + quicksort(right)
    
myList = [23, 2, 52, 63, 46, 42, 12]
print("MyList is", myList)
print(quicksort(myList))
