from bisect import bisect_left

list_of_words = ["Apple", "Banana", "Carrot", "Kiwi", "Orange","Orbnge", "Zuccini"]
target_word = "Orbnge"


def binary_search(lista, worda):
    left = 0
    right = len(lista) - 1
    while left <= right:
        middle = (left + right) // 2
        mid_word = lista[middle]
        if worda == mid_word:
            return True
        elif worda > mid_word:
            left = middle + 1
        else:
            right = middle - 1
    return False


print(binary_search(list_of_words, target_word))

def binary_search_bised(lista,worda):
    index=bisect_left(lista,worda)
    if index<len(lista) and lista[index]==worda:
        return index
    return -1

print(binary_search_bised(list_of_words,"Orange"))

