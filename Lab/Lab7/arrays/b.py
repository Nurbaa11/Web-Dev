my_list = []
size = int(input())
for _ in range(size):
    value = int(input())
    if(value % 2 == 0):
        my_list.append(value)
print(my_list)
