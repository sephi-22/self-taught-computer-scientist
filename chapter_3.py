#Linear time search algorithm(Linear Search)
def linear_search(list,n):
    for i in list:
        if i == n:
            return True
    return False

myList = [1,2,3,4,5,6,7,8,9,10]
print(linear_search(myList,10))
print(linear_search(myList,20))

#Using Python's built-in keyword instead.
unsorted_list = [24,12,23,25,64,75,11,14,125]
print(11 in unsorted_list)
print('a' in 'snapple')