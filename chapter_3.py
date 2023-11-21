# Linear time search algorithm(Linear Search)
def linear_search(list, n):
    for i in list:
        if i == n:
            return True
    return False


# The Linear Search but pythonic way.
def linear_search_pythonic(lst, n):
    return any(x == n for x in lst)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(linear_search_pythonic(myList, 10))
print(linear_search_pythonic(myList, 20))

# Using Python's built-in keyword instead.
unsorted_list = [24, 12, 23, 25, 64, 75, 11, 14, 125]
print(11 in unsorted_list)
print("a" in "snapple")


# Binary Search
def binary_search(lst, n):
    first = 0
    last = len(lst) - 1
    while first <= last:
        middle = (first + last) // 2
        if lst[middle] == n:
            return True
        else:
            if n < lst[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return False


print(binary_search(myList, 11))

# Binary search using Python's own module.
from bisect import bisect_left

print(bisect_left(myList, 9))


# Writing proper bisect_left function.
def binary_search_bisect(an_iterable, target):
    index = bisect_left(an_iterable, target)
    if (
        index < len(an_iterable) and an_iterable[index] == target
    ):  # I changed this from <= to <
        return True
    return False


print(binary_search_bisect(myList, 8))

print(ord("a"))
print(ord("x"))


# Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list.
def binary_search_words(word_list, target_word):
    def compare_words(word1, word2):
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if ord(word1[i]) < ord(word2[i]):
                return -1
            elif ord(word1[i]) > ord(word2[i]):
                return 1
        return 0 if len(word1) == len(word2) else -1 if len(word1) < len(word2) else 1

    left, right = 0, len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = word_list[mid]

        comparison = compare_words(mid_word, target_word)

        if comparison == 0:
            return True
        elif comparison < 0:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Binary search (implicit Ord)
def binary_search_implicit(word_list, target_word):
    left, right = 0, len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_word = word_list[mid]

        if mid_word == target_word:
            return True
        elif mid_word < target_word:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Binary Search (Words) using Bisect


def binary_search_words_bisect(word_list, target_word):
    index = bisect_left(word_list, target_word)
    return index < len(word_list) and word_list[index] == target_word


# Example usage:
word_list = ["apple", "banana", "grape", "orange", "pear", "watermelon"]
target_word = "orange"

result = binary_search_implicit(word_list, target_word)

if result:
    print(f"The word '{target_word}' is in the list.")
else:
    print(f"The word '{target_word}' is not in the list.")
