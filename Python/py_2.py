import time

lst = ['suresh', 'aman', 'akash', 'pritam', 'santosh', 'suresh', 'akash']

start = time.time()
# lst.sort(reverse=True)
# print(lst)


# operation 3 or 8
lst2 = [] # operation 1
for i in lst: # operation 2
    if i not in lst2:
        lst2.append(i) # operation 3, 4
for j in range(len(lst2)): # operation 5
    for k in range(len(lst2)): # operation 6
        if lst2[j] < lst2[k]:
            lst2[j], lst2[k] = lst2[k], lst2[j] # operation 7, 8

print(lst2)
print(time.time() - start)


print()
start = time.time()
lst = list(sorted(set(lst))) # operation 1, 2, 3
print(lst)
print(time.time() - start)

def operation(x, j = 0):
    j = str(x * x) + 'Code'
    operation.preserve = j
    return x

operation(x = 5)
print(operation.preserve)
