def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x) - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

my_list = [25, 50, 0]
bubble_sort(my_list)
print(my_list)