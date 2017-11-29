import random

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

for elem in lst:
    elem *= 2
    print(elem)

print(lst)

print('---1---')
for i, elem in enumerate(lst):
    print(i, elem)
    lst[i] *= 2

# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])

print('---2---')
zeros_lst = [0] * 100

def multiply_list(lst, coeff):
    for i in range(len(lst)):
        lst[i] *= coeff

def fill_list(lst, lower_bound, upper_bound):
    for i in range(len(lst)):
        lst[i] = random.randint(lower_bound, upper_bound)

def nullify_list(lst):
    for i in range(len(lst)):
        lst[i] = 0


print(id(zeros_lst), zeros_lst)

fill_list(zeros_lst, 10, 20)
print(id(zeros_lst), zeros_lst)

multiply_list(zeros_lst, 20)
print(id(zeros_lst), zeros_lst)

nullify_list(zeros_lst)
print(id(zeros_lst), zeros_lst)