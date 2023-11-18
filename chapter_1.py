#printing 5 elements from a list and timing it
import time
start = time.time()
for i in range(1,6000):
    print(i)
end = time.time()
print(end-start)