import random

# x = 10
#
# while x > 0:
#     print("Hello world!", x)
#     x -= 1
#
# x = 10
# while x < 100:
#     print("Hello world!", x)
#     x += random.randint(0, 5)


# def fill_truck(volume_capacity, lower_bound, upper_bound):
#     current_capacity = 0
#
#
#     while current_capacity < volume_capacity:
#         random_box = random.randint(lower_bound, upper_bound)
#         if random_box <= (volume_capacity - current_capacity):
#
#            current_capacity += random_box
#            print("Current capacity = %d, last box = %d" % (current_capacity, random_box))
#         else:
#             print("Skipped box %d" % random_box)
#
# fill_truck(1000, 1, 20)

print("Привет, Богатырь!")
print("1: Налево пойдешь - коня потеряешь")
print("2: Направо пойдешь - пол царства найдешь")
print("3: Прямо пойдешь - мешок денег найдешь")


while True:
    user_choise = input("Сделай свой выбор [1..3], q - выход")
    #1
    # print(user_choise)

    if user_choise == "q":
        print("Заходи еще!")
        break1

    if user_choise == "1":
        print("Лошадку жалко :(")

    elif user_choise == "2":
        print("Молодец!")

    elif user_choise == "3":
        print("10% за подсказку")

    else:
        print("Сделай правильный выбор")