#Array of functions that returns an array of integers from n to 1 where n>0
def reverse_count(n):
    if n==0:
        return []
    return [n]+reverse_count(n-1)

print(reverse_count(5))

